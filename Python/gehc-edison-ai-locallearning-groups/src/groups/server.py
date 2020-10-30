"""
This file stores all the LDAP server information
server URL : URL of the LDAP server
port no : 389 (default port no)
"""

import os
from flask import Flask

# Server information
HOST_NAME = '3.28.94.47'
PORT_NO = '32046'

# Server Domain
DOMAIN = 'cn=admin,dc=example,dc=org'
PASSWORD = 'admin'
SEARCH_BASE = 'dc=example,dc=org'

# server uri
server_uri = f"ldap://{HOST_NAME}:{PORT_NO}"
#server_uri = f"ldap://ldap-openldap:389"
#server_uri = os.environ['LDAP_URI']


