#!/usr/bin/env bash
apt-get -y update
apt-get install -y python-dev libldap2-dev libsasl2-dev libssl-dev
apt-get install build-essential python3-dev \
    libldap2-dev libsasl2-dev slapd ldap-utils python-tox \
    lcov valgrind