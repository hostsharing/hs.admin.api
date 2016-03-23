""" This module provides class that provides information to dispatches to the relevant backend.
"""


class Dispatcher(object):
    """ This class provides information to dispatch to the relevant backend.
    """

    def __init__(self, modules):
        self.modules = modules


    def get_backend(self, module):
        """ Returns the backend which is relevant for the remote module """

        return self.modules[module]


    def get_backends(self):
        """ Returns the list of available backends """

        return set(self.modules.values())


    def get_modules(self):
        """ Returns the list of available remote modules """

        return set(self.modules.keys())
