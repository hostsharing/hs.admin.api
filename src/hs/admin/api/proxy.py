""" This module provides a directly callable class that implements a remote method invokation.
"""

try:
    from xmlrpclib import ServerProxy
    from xmlrpclib import Fault
except ImportError:
    from xmlrpc.client import ServerProxy
    from xmlrpc.client import Fault

from .exceptions import ProxyError



class Proxy(object):
    """ This directly callable class implements a remote method invokation.
    """

    def __init__(self, session, dispatcher):
        self.session = session
        self.dispatcher = dispatcher


    def __call__(self, module, method, where=None, set=None):
        backend = self.dispatcher.get_backend(module)
        remote = getattr(ServerProxy(backend), module + '.' + method)
        ticket = self.session.get_ticket()
        user = self.session.get_user()

        try:
            if (where is None) and (set is None):
                result = remote(user, ticket)
            elif where is None:
                result = remote(user, ticket, set)
            elif set is None:
                result = remote(user, ticket, where)
            else:
                result = remote(user, ticket, set, where)

        except Fault as fault:
            raise ProxyError(fault.faultString)

        return result
