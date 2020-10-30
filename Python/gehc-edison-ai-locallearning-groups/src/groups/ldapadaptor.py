import ldap
import ldap.modlist as modlist
import json
from src.groups.server import server_uri,DOMAIN,PASSWORD,SEARCH_BASE
from src.groups.logger import LDAPLogger
from src.groups.edisonexception import EdisonLDAPException


from collections import defaultdict
from ldap3 import Server, Connection, ALL, SUBTREE, MODIFY_ADD, MODIFY_REPLACE, ObjectDef, ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES
from ldap3.core.exceptions import LDAPException, LDAPBindError
from ldap3.extend.microsoft.addMembersToGroups import ad_add_members_to_groups


LOG = LDAPLogger.get_logger("ldapadaptor.py","INFO")


def _get_ldap_attrs():
    LDAP_Attr = defaultdict(lambda : "None")
    return LDAP_Attr


def connect_ldap_server():
    """
    :return: Bool value : True if connection successful , LDAPException is connection fails
    """

    try:
        LOG.info(f' Initiating connection to LDAP Server {server_uri}')
        server = Server(server_uri, get_info=ALL)
        LOG.debug(f' The LDAP domain is {DOMAIN}')
        connection = Connection(server, user=DOMAIN, password=PASSWORD)
        bind_response = connection.bind()
        LOG.info(f" LDAP server bind response {bind_response} ")
    except LDAPBindError as e:
        connection = e
        LOG.error(f' Error while establishing LDAP Connection {connection}')
    finally:
        LOG.info(f' Connection response to LDAP server {connection}')
        return connection


def get_ldap_users(username=None):
    """
    :param username: The user id number to search
    :return: user information with cn, givenName, uidNumber and uid
    """
    LOG.info(f' Fetching LDAP users ')
    search_base = SEARCH_BASE

    if username is None:
        LOG.info(f' uid value is *. Fetching all the users ')
        search_filter = '(&(objectClass=inetOrgPerson))'
    else:
        LOG.info(f' Fetching user information for username {username}')
        search_filter = '(&(objectClass=inetOrgPerson)(cn={}))'.format(username)

    connection = connect_ldap_server()
    try:
        LOG.info(f" Searching LDAP server with search filter {search_filter} ")
        connection.search(search_base=search_base, search_filter=search_filter,
                          search_scope=SUBTREE,
                          attributes=['cn','gidNumber','uidNumber','sn','uid'])
        results = connection.entries
        LOG.info(f" The results are {results} ")
    except LDAPException as e:
        results = e
        LOG.error(f" Error while fetching user information {results} ")
    connection.unbind()
    return results


def get_ldap_groups(group_name = None):
    """
    :param group_name:
    :return:
    """
    search_base = SEARCH_BASE
    if group_name is None:
        LOG.info(f' groupname is set to *. Fetching all groups ')
        search_filter = '(&(objectClass=posixGroup))'
    else:
        LOG.info(f' Fetching group with groupname {group_name} ')
        search_filter = '(&(objectClass=posixGroup)(cn={}))'.format(group_name)

    LOG.info(f" Searching with filter {search_filter} ")
    connection = connect_ldap_server()
    try:
        connection.search(search_base=search_base,
                          search_filter=search_filter,
                          search_scope=SUBTREE,
                          attributes=['cn','gidNumber'])
        results = connection.entries
        LOG.info(f" Group search results {results} ")
    except LDAPException as e:
        results = e
        LOG.error(f' Error while fetching group information {results} ')
    connection.unbind()
    return results


def add_ldap_group(group_id, group_name):
    """
    :param group_id:
    :return:
    """

    # set all the group attributes
    ldap_attr = _get_ldap_attrs()
    ldap_attr['objectClass'] = get_group_object()
    ldap_attr['gidNumber'] = group_id

    # Bind connection to LDAP server
    ldap_conn = connect_ldap_server()
    if not type(ldap_conn) == Connection:
        raise EdisonLDAPException(" Error while connecting to LDAP server ")

    LOG.info(f'The LDAP connection response is {ldap_conn}')
    group_dn = "cn={},ou=EdisonAI,dc=example,dc=org".format(group_name)

    try:
        LOG.info(f' Adding group information with dn {group_dn}')
        response = ldap_conn.add(dn=group_dn,
                                 attributes=ldap_attr)
        LOG.info(f' Group addition response {ldap_conn.result} ')
    except LDAPException as e:
        LOG.error(f' Error while adding group {e}')
        response = (" The error is ", e)
    ldap_conn.unbind()
    return response


def add_new_user_to_group(group_id,user_id,user_name,sur_name):
    """
    :param group_id:
    :param user_id:
    :param user_name:
    :return:
    """
    ldap_attr = _get_ldap_attrs()
    ldap_attr['cn'] = user_name
    ldap_attr['sn'] = sur_name
    ldap_attr['uid'] = user_name + " " + sur_name
    ldap_attr['uidNumber'] = user_id
    ldap_attr['gidNumber'] = group_id
    ldap_attr['homeDirectory'] = '/home/users/{}'.format(user_name)

    # Bind connection to LDAP server
    ldap_conn = connect_ldap_server()

    group_name = get_group_name(group_id)

    LOG.info(f" Group name is {group_name}.Adding user to group ")
    user_dn = "cn={},cn={},ou=EdisonAI,dc=example,dc=org".format(user_name, group_name)

    LOG.info(f' User dn to be added {user_dn}')

    try:
        LOG.info(f' Adding user with dn {user_dn}')

        response = ldap_conn.add(dn=user_dn,
                                 object_class=['top', 'posixAccount', 'inetOrgPerson'],
                                 attributes=ldap_attr)
        LOG.info(f' User add response is {ldap_conn.result} ')
    except LDAPException as e:
        response = e
        LOG.error(f' Error while adding user to group {response} ')
    return response


def add_existing_user_to_ldapgroup(user_name, user_id, group_name, group_id):
    """
    :return:
    """

    converted_user_name = bytes(user_name, 'utf-8')
    converted_user_id = bytes(user_id, 'utf-8')
    converted_group_name = bytes(group_name, 'utf-8')
    converted_group_id = bytes(str(group_id),'utf-8')

    ldap_attr = _get_ldap_attrs()
    ldap_attr['uid'] = converted_user_name
    ldap_attr['cn'] = converted_user_name
    ldap_attr['uidNumber'] = converted_user_id
    ldap_attr['gidNumber'] = converted_group_id
    ldap_attr['objectClass'] =  [b'top', b'inetOrgPerson', b'posixAccount']
    ldap_attr['sn'] = b'kumar'
    ldap_attr['homeDirectory'] = b'/home/users/dkumar'
    #group_name = get_group_name(group_id)

    LOG.info(f' The group name for id {group_id} is {group_name}')

    conn = ldap.initialize(server_uri, bytes_mode=False)
    conn.simple_bind_s(DOMAIN,PASSWORD)
    dn_new = "cn={},cn={},ou=EdisonAI,dc=example,dc=org".format(user_name,group_name)
    ldif = modlist.addModlist(ldap_attr)
    try:
        response = conn.add_s(dn_new, ldif)
    except ldap.error as e:
        LOG.error(f" Error while adding user to group {e} ")
        response = e
    finally:
        conn.unbind()
        LOG.info(f" The user addition response is {response} ")
        return response




def get_ldap_group_from_group_id(group_id):

    search_base = SEARCH_BASE
    if group_id is None:
        LOG.info(f' groupname is set to *. Fetching all groups ')
        search_filter = '(&(objectClass=posixGroup))'
    else:
        LOG.info(f' Fetching group with groupid {group_id} ')
        search_filter = '(&(objectClass=posixGroup)(gidNumber={}))'.format(group_id)

    LOG.info(f" Searching with filter {search_filter} ")
    connection = connect_ldap_server()
    try:
        connection.search(search_base=search_base,
                          search_filter=search_filter,
                          search_scope=SUBTREE,
                          attributes=ALL_ATTRIBUTES)
        results = connection.entries
        LOG.info(f" Group search results {results} ")
    except LDAPException as e:
        results = e
        LOG.error(f' Error while fetching group information {results} ')
    connection.unbind()


def get_group_name(gid):
    try:
        group_info = get_ldap_group_from_id(gid)
        results = group_info[0].cn
        LOG.info(f' Group name for group id {results}')
    except LDAPException as e:
        results = e
        LOG.error(f' Error while fetching group name for group id {results}')
    except IndexError as e:
        results = e
        LOG.error(f' Error while fetching group name for group id {results}')
    return results


def get_group_id_from_name(group_name):
    try:
        ldap_conn = connect_ldap_server()
        search_filter = '(&(objectClass=posixGroup)(cn={}))'.format(group_name)
        ldap_conn.search(search_base=SEARCH_BASE,
                         search_filter=search_filter,
                         search_scope=SUBTREE,
                         attributes=ALL_ATTRIBUTES)
        results = ldap_conn.entries
        LOG.info(f" The entries are {ldap_conn.entries}")
        jsonified_value = json.loads(results[0].entry_to_json())
        response = jsonified_value.get("attributes").get("gidNumber").pop()
        LOG.info(f" The search response is {response} ")
        return response
    except LDAPException as e:
        response = e
        LOG.info(f" Exception while searching {response} ")
    finally:
        ldap_conn.unbind()


def get_ldap_group_from_id(group_id):
    search_base = SEARCH_BASE
    search_filter = '(&(objectClass=posixGroup)(gidNumber={}))'.format(group_id)

    LOG.info(f" Searching with filter {search_filter} ")
    connection = connect_ldap_server()
    try:
        connection.search(search_base=search_base,
                          search_filter=search_filter,
                          search_scope=SUBTREE,
                          attributes=['cn', 'gidNumber'])
        results = connection.entries
        LOG.info(f" Group search results {results} ")
    except LDAPException as e:
        results = e
        LOG.error(f' Error while fetching group information {results} ')
    connection.unbind()
    return results


def delete_user_from_ldap(user_name=None, group_name=None):
    """
    :param attribute_id: user or group id
    :return: True if success/False if deletion failed
    """

    default_group = get_default_group()
    #user_dn = get_dn_from_id(attribute_id)

    # connect to the ldap server
    conn = connect_ldap_server()
    LOG.info(f" User name is {user_name} ")
    if user_name is not None:
        LOG.info(f" Initiating deletion for user {user_name} from {group_name} ")
        user_dn = 'cn={},cn={},ou=EdisonAI,dc=example,dc=org'.format(user_name,group_name)
    else:
        LOG.info(f" Initiating deletion for group {group_name} ")
        user_dn = 'cn={},ou=EdisonAI,dc=example,dc=org'.format(group_name)

    #user_cn = user_dn.split(',')[0]
    LOG.info(f" Deleting dn {user_dn} ")

    try:
        response = conn.delete(dn=user_dn)
        LOG.info(f" Delete user info {conn.result}")
    except LDAPException as e:
        response = e
        LOG.error(f" Error while deleting {response}")
    finally:
        LOG.info(f" Returning response for deletion {response} ")
        conn.unbind()
        return response


def get_group_object():
    return ['posixGroup','top']


def get_user_object():
    return ['inetOrgPerson','posixAccount','top']


def get_default_group():
    return 'cn=Alluser,ou=EdisonAI,dc=example,dc=org'


def get_dn_from_id(ldap_id):
    """
    :param ldap_id: user id or group id
    :return: distingushed name for user/group
    """
    LOG.info(f" Getting dn for id {ldap_id} ")
    results = get_ldap_users(ldap_id)
    LOG.info(f" The db search results for username {ldap_id} is {results}")
    for result in results:
        json_result = json.loads(result.entry_to_json()).get("dn")
    LOG.info(f" Returning dn {json_result} for id {ldap_id}")
    return json_result


def get_ldap_group_members(group_name=None):
    """
    :param group_name:
    :return:
    """
    search_base = 'cn={},ou=EdisonAI,dc=example,dc=org'.format(group_name)
    search_filter = '(&(objectClass=inetOrgPerson))'

    LOG.info(f" Searching with filter {search_filter} ")
    connection = connect_ldap_server()
    try:
        connection.search(search_base=search_base,
                          search_filter=search_filter,
                          search_scope=SUBTREE,
                          attributes=['cn','gidNumber','uidNumber','sn','uid'])
        results = connection.entries
        LOG.info(f" Group search results {results} ")
    except LDAPException as e:
        results = e
        LOG.error(f' Error while fetching group information {results} ')
    connection.unbind()
    return results




# def add_nested_group(group_id):
#     """
#     :return:
#     """
#     # set all attributes
#     ldap_attr = _get_ldap_attrs()
#     ldap_attr['objectClass'] = get_group_object()
#     ldap_attr['gidNumber'] = group_id
#
#     # bind connection to LDAP server
#     ldap_conn = connect_ldap_server()
#
#     if not type(ldap_conn) == Connection:
#         raise EdisonLDAPException(" Error while connecting to LDAP server ")
#
#     LOG.info(f'The LDAP connection response is {ldap_conn}')
#     nested_group_dn = "cn={},cn={},dc=example,dc=com".format("group3","group6")
#
#     try:
#         LOG.info(f' Adding group information with dn {nested_group_dn}')
#         response = ldap_conn.add(nested_group_dn, attributes=ldap_attr)
#     except LDAPException as e:
#         LOG.error(f' Error while adding group {e}')
#         response = (" The error is ", e)
#     ldap_conn.unbind()
#     return response

