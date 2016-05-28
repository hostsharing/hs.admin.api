""" This module provides a class that implements the HSAdmin API.
"""

try:
    from xmlrpclib import ServerProxy
except ImportError:
    from xmlrpc.client import ServerProxy

from .dispatcher import Dispatcher
from .session import Session
from .proxy import Proxy
from .module import Module



class API(object):
    """ This class implements the HSAdmin API.
    """

    def __init__(self, cas, credentials, backends):
        session = Session(cas['uri'],
                          cas['service'],
                          credentials['username'],
                          credentials['password'])

        modules = dict()
        meta = dict()
        for backend in backends:
            remote = getattr(ServerProxy(backend), 'property.search')
            props = remote(session.get_user(), session.get_ticket(), dict())
            meta[backend] = dict()
            for module in set([prop['module'] for prop in props]):
                modules[module] = backend
                meta[backend][module] = dict()
                for prop in [prop for prop in props
                             if ('module' in prop) and (prop['module'] == module)]:
                    del prop['module']
                    meta[backend][module][prop['name']] = prop

        dispatcher = Dispatcher(modules)
        proxy = Proxy(session, dispatcher)

        self.modules = dict()
        for module in dispatcher.get_modules():
            self.modules[module] = Module(proxy,
                                          module,
                                          meta[dispatcher.get_backend(module)][module],
                                          ['search', 'add', 'update', 'delete'])
            setattr(self, module, self.modules[module])


    def list_modules(self):
        """ Return the list of modules """

        return self.modules.keys()


    def get_module(self, name):
        """ Returns a module instance by name """

        return self.modules[name]

