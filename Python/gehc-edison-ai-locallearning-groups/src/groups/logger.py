import logging
from ldap3.utils.log import (set_library_log_detail_level, set_library_log_hide_sensitive_data, \
                            BASIC, EXTENDED)

class LDAPLogger(object):

    _LOG = {"INFO":logging.INFO, "ERROR":logging.ERROR, "WARNING":logging.WARNING,
            "DEBUG":logging.DEBUG}

    @staticmethod
    def _init_logger(file_name, log_level):
        ldap_logger = logging.getLogger(file_name)
        logging.basicConfig(level=logging.INFO)
        ldap_logger.setLevel(LDAPLogger._LOG.get(log_level))
        set_library_log_hide_sensitive_data(hide=True)
        if log_level == "INFO":
            set_library_log_detail_level(detail=BASIC)
        elif log_level == "DEBUG":
            set_library_log_detail_level(detail=EXTENDED)
        return ldap_logger

    @staticmethod
    def get_logger(file_name, log_level):
        ldap_log = LDAPLogger._init_logger(file_name, log_level)
        return ldap_log

