""" This module provides a class that representing a remote module.
"""

from .method import Method



class Module(object):
    """ This class represents a remote module.
    """

    def __init__(self, proxy, name, properties, methods):
        self.name = name
        self.properties = properties

        self.methods = dict()
        for method in methods:
            self.methods[name] = Method(proxy, self, method)
            setattr(self, method, self.methods[name])


    def list_methods(self):
        """ Returns the list of methods """

        return self.methods.keys()


    def get_method(self, name):
        """ Returns a method instance by name """

        return self.methods[name]


    def list_properties(self):
        """ Returns the list of properties """

        return self.properties.key()


    def get_property(self, name):
        """ Returns a property instance by name """

        return self.properties[name]
