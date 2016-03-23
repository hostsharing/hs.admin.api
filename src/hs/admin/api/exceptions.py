""" This module provides exception classes.
"""



class LoginError(Exception):
    """ Raised when the login failed.
    """


class SessionError(Exception):
    """ Raised when the session failed.
    """


class ProxyError(Exception):
    """ Raised when an remote backend invokation failed.
    """
