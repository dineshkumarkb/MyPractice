from unittest.mock import Mock, patch
from ldap3.core.exceptions import LDAPBindError
from ldap3 import Connection, Server, MOCK_SYNC
import pytest
from collections import defaultdict
from src.groups.ldapadaptor import (connect_ldap_server, add_nested_group, add_existing_user_to_ldapgroup,
                                    get_user_object, get_group_name, get_ldap_users)

test_ldap_attr = defaultdict(lambda : "None")


def test_connect_ldap_server():
    response = connect_ldap_server()
    assert isinstance(response, Connection)


def test_add_nested_group():
    server = Server('testserver')
    connection = Connection(server, client_strategy=MOCK_SYNC)
    connection.strategy.add_entry('cn=user1,ou=test,o=lab',
                                  {'userPassword': 'test1111', 'sn': 'user1_sn', 'revision': 0})
    add_nested_group('501')


def test_add_existing_user_to_ldap_group():
    server = Server('testserver')
    connection = Connection(server, client_strategy=MOCK_SYNC)
    connection.strategy.add_entry('cn=user1,ou=test,o=lab',
                                  {'userPassword': 'test1111', 'sn': 'user1_sn', 'revision': 0})
    add_existing_user_to_ldapgroup('testuser','500','501')


def test_get_user_object():
    assert get_user_object() == ['inetOrgPerson','posixGroup','top']


def test_get_group_name_error():
    server = Server('testserver')
    connection = Connection(server, client_strategy=MOCK_SYNC)
    connection.bind()
    get_group_name('50000')


def test_get_group_name():
    server = Server('testserver')
    connection = Connection(server, client_strategy=MOCK_SYNC)
    connection.bind()
    get_group_name('500')


def test_get_ldap_users():
    server = Server('testserver')
    connection = Connection(server, client_strategy=MOCK_SYNC)
    connection.bind()
    get_ldap_users('500')


