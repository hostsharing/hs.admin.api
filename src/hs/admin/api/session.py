""" This module provides a class that implements a remote user session.
"""

from requests import delete, post
from yaml import safe_load


class Session(object):
    """ This class implements a remote user session.
    """

    def __init__(self, provider, service, username, password):
        payload = {'username': username,
                   'password': password}
        result = post(provider, data=payload)
        if result.status_code != 201:
            raise Exception('Session Error: Acquisition of ticket granting ticket failed.')
        self.service = service
        self.tgt = result.headers['location']
        self.user = username

    def __exit__(self, exc_type, exc_value, traceback):
        delete(self.tgt)

    def get_ticket(self):
        """ Returns a one-time ticket for a remote user action """

        payload = {'service': self.service}
        result = post(self.tgt, data=payload)
        if result.status_code != 200:
            raise Exception('Session Error: Acquisition of session ticket failed.')
        return safe_load(result.text)

    def get_user(self):
        """ Returns the name of the user """

        return self.user
