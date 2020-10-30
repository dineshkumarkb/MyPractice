from src.groups import get_user_data
from src.groups import add_existing_user_to_ldapgroup, _get_group_id, _get_user_id, create_user
from src.groups.api import create_user
import pytest
from unittest.mock import Mock
from unittest.mock import patch
import src
import json

all_user_data = {
    "Dinesh Kumar": {
        "attributes": {
            "cn": [
                "Dinesh Kumar"
            ],
            "sn": [
                "Kumar"
            ],
            "uid": [
                "dkumar"
            ],
            "uidNumber": [
                1000
            ]
        },
        "dn": "cn=Dinesh Kumar,cn=devops,ou=EdisonAI,dc=testldap,dc=com"
    }
}

all_group_data = {'Dinesh Kumar': {'attributes': {'cn': ['Dinesh Kumar'], 'gidNumber': [500]}, 'dn': 'cn=Dinesh Kumar,cn=devops,ou=EdisonAI,dc=testldap,dc=com'}, 'agni': {'attributes': {'cn': ['agni'], 'gidNumber': [1052]}, 'dn': 'cn=agni,ou=EdisonAI,dc=testldap,dc=com'}, 'devops': {'attributes': {'cn': ['devops'], 'gidNumber': [501]}, 'dn': 'cn=devops,ou=EdisonAI,dc=testldap,dc=com'}, 'training': {'attributes': {'cn': ['training'], 'gidNumber': [500]}, 'dn': 'cn=training,ou=EdisonAI,dc=testldap,dc=com'}, 'workbench': {'attributes': {'cn': ['workbench'], 'gidNumber': [502]}, 'dn': 'cn=workbench,ou=EdisonAI,dc=testldap,dc=com'}}
user_id_range = [x for x in range(2000,3000)]
group_id_range = [x for x in range(1000,2000)]

def test_get_user_data(flasky):
    client = flasky.test_client()
    test_url = '/ldap/v1/users/'
    assert client.get(test_url).status_code == 200


@patch('src.groups.api.get_user_data')
def test_get_user_data_mock(mock_get_user_data):
    mock_get_user_data.return_value = all_user_data
    response = mock_get_user_data()
    assert response == all_user_data

@patch('src.groups.api.get_user_data')
def test_get_user_data_mock(mock_get_user_data):
    mock_get_user_data.return_value = all_user_data
    response = mock_get_user_data()
    assert response == all_user_data


def test_get_group_data_mock():
    mock_flask = Mock()
    mock_flask.get_group_data.return_value = all_group_data
    response = mock_flask.get_group_data()
    assert response == all_group_data


def test_get_group_data_status(flasky):
     client = flasky.test_client()
     test_url = '/ldap/v1/groups/'
     response = client.get(test_url)
     assert response.status_code == 200



def test_create_user(flasky):
    client = flasky.test_client()
    test_url = '/ldap/v1/users:CREATE'
    mock_request_headers = {}

    mock_request_data = {'body':{
        'username':'Edison User'
    }
    }
    assert isinstance(client.post(test_url, data=json.dumps(mock_request_data),
                                  headers = mock_request_headers).status_code,int)


def test_create_group(flasky):
    client = flasky.test_client()
    test_url = '/ldap/v1/groups:CREATE'
    mock_request_headers = {}

    mock_request_data = {'body':{
        'groupname':'Edison User'
    }
    }
    assert isinstance(client.post(test_url, data=json.dumps(mock_request_data),
                                  headers = mock_request_headers).status_code,int)


def test_add_existing_user_to_grp(flasky):
    client = flasky.test_client()
    test_url = '/ldap/v1/groups/500/users:ADD'
    mock_request_headers = {}

    mock_request_data = {'body': {
        'username': 'Edison User'
    }}
    assert isinstance(client.put(test_url,data=json.dumps(mock_request_data),
                                 headers=mock_request_headers).status_code, int)


def test_group_id():
    assert _get_group_id() in group_id_range


def test_user_id():
    assert _get_user_id() in user_id_range








