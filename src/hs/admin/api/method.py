""" This module provides a directly callable class that implements a remote method.
"""



class Method(object):
    """ This directly callable class implements a remote method.
    """

    def __init__(self, proxy, module, name):
        self.module = module
        self.name = name
     
        self.__class__.__call__ = lambda self, where=None, set=None: proxy(self.module.name,
                                                                           self.name,
                                                                           where,
                                                                           set)
