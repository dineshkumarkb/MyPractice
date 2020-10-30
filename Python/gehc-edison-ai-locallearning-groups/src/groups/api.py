import sys
sys.path.append('.')
from src.groups.logger import LDAPLogger
from src.groups.ldapadaptor import (get_ldap_users, add_ldap_group,
                                    add_new_user_to_group, get_ldap_groups,
                                    add_existing_user_to_ldapgroup,
                                    delete_user_from_ldap,
                                    get_ldap_group_members)
from src.groups.edisonexception import (EdisonLDAPException,EdisonLDAPOperationDeniedException,
                                        EdisonLDAPUserExistsException, EdisonLDAPUnprocessableEntityException,
                                        err)


from flask import request, jsonify, abort, Flask
import random
import json
import jwt, os

# initiate logging for this file
LOG = LDAPLogger.get_logger(os.path.basename(__file__), 'INFO')

app = Flask(__name__)


@app.route("/ldap/v1/users/", methods=['GET'])
def get_user_data():
    """
    :return:
    """
    query_params = request.query_string.decode('utf-8')
    user_id = None
    final_list = []
    LOG.info(f" Received GET request {query_params} ")

    if query_params:
        query_key = query_params.split("=")[0]
        if query_key != 'loginName':
            raise EdisonLDAPUnprocessableEntityException(" Incorrect query string parameter ")
        user_id = request.args.get('loginName')
        LOG.info(f" Received user id {user_id} ")

    results = get_ldap_users(user_id)

    LOG.info(f" Returned results are {results} ")

    # list is ordered with dict return order to match the values.DO NOT Change the order.
    params_list = ["loginName", "groupId", "displayName", "familyName", "userId"]

    for result in results:
        jsonified_result = result.entry_to_json()
        LOG.info(f" The jsonified result is {jsonified_result}")
        attr_json = json.loads(jsonified_result).get('attributes')
        # Extract the dn for the group name
        dn_json = json.loads(jsonified_result).get("dn")
        # Extract the group name from the dn
        group_name = dn_json.split(",")[1].split("=")[1]
        temp_dict = {k:str(v.pop()) for k,v in attr_json.items()}
        # From python 3.6 dict preserves the insertion order
        final_dict = (dict(zip(params_list,list(temp_dict.values()))))
        final_dict["groupName"] = group_name
        final_list.append(final_dict)
        del temp_dict,final_dict
    response = app.response_class(response=json.dumps({"users":final_list}, default=str, indent=4),
                                  status=200,
                                  mimetype='application/json')
    return response


@app.route("/ldap/v1/groups/", methods=['GET'])
def get_group_data():
    """
    :return:
    """

    group_name = request.args.get('groupName')
    results = get_ldap_groups(group_name)
    LOG.info(f" Getting group information with group id {group_name} ")
    final_list = []
    params_list = ["groupName","groupId"]
    for result in results:
        result_json = json.loads(result.entry_to_json()).get('attributes')
        temp_dict = {k: str(v.pop()) for k, v in result_json.items()}
        final_dict = dict(zip(params_list,temp_dict.values()))
        final_list.append(final_dict)
        del final_dict
    sorted_final_list = sort_list_dictionary(final_list,"groupName")
    response = app.response_class(response=json.dumps({"groups": sorted_final_list}, default=str, indent=4),
                                  status=200,
                                  mimetype = 'application/json')
    return response


@app.route("/ldap/v1/group/members/", methods=['GET'])
def get_group_member_data():
    """
    :return:
    """
    group_name = request.args.get('groupName')
    results = get_ldap_group_members(group_name)
    LOG.info(f" Getting group information with group id {group_name} ")
    final_list = []
    params_list = ["loginName", "groupId", "displayName", "familyName", "userId"]
    for result in results:
        result_json = json.loads(result.entry_to_json()).get('attributes')
        temp_dict = {k: v.pop() for k, v in result_json.items()}
        final_dict = dict(zip(params_list,temp_dict.values()))
        final_list.append(final_dict)
        del final_dict
    response = app.response_class(response=json.dumps({"groupMembers": final_list}, default=str, indent=4),
                                  status=200,
                                  mimetype='application/json')

    return response


@app.route("/ldap/v1/groups/users:ADD", methods=['PUT'])
def add_existing_user_to_group():
    """
    :return:
    """
    json_body = json.loads(request.data)
    user_name = json_body.get("loginName")
    group_name = json_body.get("groupName")
    user_id = json_body.get("userId")
    group_id = json_body.get("groupId")
    LOG.info(f' Adding user {user_name} to the group {group_name} ')
    results = add_existing_user_to_ldapgroup(user_name, user_id, group_name, group_id)
    if type(results) is tuple:
        response = app.response_class(response=json.dumps({"users":"Success"}, default=str, indent=4),
                                      status=200,
                                      mimetype='application/json')
        return response
    else:
        raise EdisonLDAPUserExistsException(results)


@app.route("/ldap/v1/groups:CREATE", methods=["POST"])
def create_group():
    group_id = str(_get_group_id())
    json_body = json.loads(request.data)
    group_name = json_body.get("groupName")
    LOG.info(f' Adding LDAP group {group_name} with id {group_id} ')
    value = add_ldap_group(group_id=group_id,
                           group_name=group_name)
    if value:
        response_value = {"groupCreation":"Success",
                          "groupId":group_id}
        response = app.response_class(response=json.dumps(response_value, indent=4, default=str),
                                      status=200,
                                      mimetype='application/json')
        return response
    else:
        raise EdisonLDAPException(value)


@app.route("/ldap/v1/users:CREATE", methods = ["POST"])
def create_user():
    user_id = str(_get_user_id())
    request_headers = request.headers.get("Authorization")
    decoded_headers = decode_jwt_token(request_headers)
    LOG.info(f" The decoded headers are {decoded_headers} ")
    request_body = json.loads(request.data)
    user_name = decoded_headers.get("sub")
    given_name = decoded_headers.get("given_name")
    group_id = request_body.get("groupId")
    LOG.info(f' Creating user with username {user_name} ')
    value = add_new_user_to_group(group_id=group_id,
                                  user_id=user_id,
                                  user_name=user_name,
                                  sur_name=given_name)
    if value:
        response_value = {"userCreation":"Success",
                          "userId":user_id}
        response = app.response_class(response=json.dumps(response_value, indent=4, default=str),
                                      status=200,
                                      mimetype='application/json')
        return response
    else:
        raise EdisonLDAPException(value)


@app.route("/ldap/v1/users/removeuser/", methods=["DELETE"])
def delete_user():
    LOG.info(f" Request received for delete user ")
    user_name = request.args.get('loginName')
    group_name = request.args.get('groupName')
    LOG.info(f" User id received {user_name} ")
    value = delete_user_from_ldap(user_name, group_name)
    if value:
        response_value = {"userDeletion":"Success"}
        response = app.response_class(response=json.dumps(response_value, indent=4, default=str),
                                      status=200,
                                      mimetype='application/json')
        return response
    else:
        raise EdisonLDAPException(value)


@app.route("/ldap/v1/groups/removegroup/", methods=["DELETE"])
def delete_group():
    group_name = request.args.get('groupName')
    LOG.info(f" Group id received {group_name} ")
    if group_name == "public":
        raise EdisonLDAPOperationDeniedException("Operation Denied.Cannot Delete a public group")
    value = delete_user_from_ldap(group_name=group_name)
    LOG.info(f" Deletion response {value} ")
    if value:
        response_value = {"groupDeletion":"Success"}
        response = app.response_class(response=json.dumps(response_value, indent=4, default=str),
                                      status=200,
                                      mimetype='application/json')
        return response
    else:
        raise EdisonLDAPOperationDeniedException(" Group Cannot deleted with member ")


def _get_group_id():
    LOG.info(f' Getting a new group id ')
    return random.randrange(1000, 2000)


def _get_user_id():
    LOG.info(f' Getting a new user id ')
    return random.randrange(2000, 3000)


def sort_list_dictionary(list_dict, key_name):
    """
    :param list_dict: List of dictionaries to be sorted
    :param key_name: key to be used to for sorting
    :return: Returns sorted list with
    """
    return sorted(list_dict, key=lambda x: x[key_name])


def decode_jwt_token(access_token):
    """
    :param access_token: access token to be decoded
    :return: decoded dictionary values
    """
    opts = {
        "verify_signature": False,
        "verify_aud": False,
        "verify_exp": False,
        "verify_at_hash": False
    }
    decoded_values = jwt.decode(access_token,'secret',options=opts)

    return decoded_values



if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.register_blueprint(err)
    app.run(host='0.0.0.0')
    LOG.info("EdisonLDAP Server started...")
