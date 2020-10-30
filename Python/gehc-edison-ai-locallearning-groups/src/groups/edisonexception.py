from flask import Flask,Blueprint, Response, jsonify


# Exception raised during LDAP Errors
class EdisonLDAPException(Exception):
    pass


# Exception raised during Flask API Errors
class EdisonLDAPUserExistsException(Exception):
    pass


class EdisonLDAPGroupExistsException(Exception):
    pass


class EdisonLDAPOperationDeniedException(Exception):
    pass


class EdisonLDAPUnprocessableEntityException(Exception):
    pass



err = Blueprint('except_app',__name__)


@err.app_errorhandler(EdisonLDAPException)
def edisonldapexception_handler(e):

    status_code = 500
    response = {
        "error": {
            'type': e.__class__.__name__,
            'message': str(e.args)
        }
    }
    return jsonify(response), status_code


@err.app_errorhandler(EdisonLDAPOperationDeniedException)
def edisonldapexception_handler(e):
    status_code = 403
    response = {
        "error": {
            'type': e.__class__.__name__,
            'message': e.args[0]
        }
    }
    return jsonify(response), status_code


@err.app_errorhandler(EdisonLDAPUnprocessableEntityException)
def edisonldapexception_handler(e):

    status_code = 422
    response = {
        "error": {
            'type': e.__class__.__name__,
            'message': str(e.args)
        }
    }
    return jsonify(response), status_code




