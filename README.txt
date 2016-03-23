Introduction
============

This package provides a Python implementation of the Hostsharing HSAdmin API.

Example
-------

>>> from hs.admin.api import API
>>> 
>>> api = API(cas=dict(uri='https://login.hostsharing.net/cas/v1/tickets',
...                    service='https://config.hostsharing.net:443/hsar/backend'),
...           credentials=dict(username='xyz00',
...                            password='top-secret'),
...           backends=['https://config.hostsharing.net:443/hsar/xmlrpc/hsadmin',
...                     'https://config2.hostsharing.net:443/hsar/xmlrpc/hsadmin'])
>>> 
>>> dir(api)
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'contact', 'customer', 'domain', 'emailaddress', 'emailalias', 'get_module', 'hive', 'list_modules', 'mandat', 'modules', 'mysqldb', 'mysqluser', 'pac', 'postgresqldb', 'postgresqluser', 'property', 'q', 'role', 'user']
>>>
>>> dir(api.mysqluser)
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'add', 'delete', 'get_method', 'get_property', 'list_methods', 'list_properties', 'methods', 'name', 'properties', 'search', 'update']
>>>
>>> print api.mysqluser.properties
{'pac': {'validationRegexp': '[a-z0-9]*', 'name': 'pac', 'searchable': 'equals', 'readwriteable': 'read', 'minLength': '0', 'displaySequence': '2', 'displayVisible': 'always', 'maxLength': '999', 'type': 'string'}, 'instance': {'validationRegexp': '[a-zA-Z]*', 'name': 'instance', 'searchable': 'equals', 'readwriteable': 'read', 'minLength': '0', 'displaySequence': '2', 'displayVisible': 'always', 'maxLength': '999', 'type': 'string'}, 'password': {'validationRegexp': "[^']{6,}", 'name': 'password', 'searchable': 'equals', 'readwriteable': 'none', 'minLength': '0', 'displaySequence': '2', 'displayVisible': 'always', 'maxLength': '999', 'type': 'string'}, 'name': {'validationRegexp': '[a-z0-9]{5}_[a-z0-9_]{1,}', 'name': 'name', 'searchable': 'equals', 'readwriteable': 'writeonce', 'minLength': '0', 'displaySequence': '1', 'displayVisible': 'always', 'maxLength': '999', 'type': 'string'}}
>>>
>>> print api.user.search()
[{'comment': 'xyz00', 'shell': '/bin/bash', 'locked': False, 'name': 'xyz00', 'quota_hardlimit': '0', 'userid': '104192', 'quota_softlimit': '0', 'pac': 'xyz00', 'id': '12110', 'homedir': '/home/pacs/xyz00'}, {'comment': 'xyz00-admin', 'shell': '/bin/bash', 'locked': False, 'name': 'xyz00-admin', 'quota_hardlimit': '0', 'userid': '104225', 'quota_softlimit': '0', 'pac': 'xyz00', 'id': '12184', 'homedir': '/home/pacs/xyz00/users/admin'}]
>>>
>>> print api.user.search(where={'name': 'xyz00-admin'})
[{'comment': 'xyz00-admin', 'shell': '/bin/bash', 'locked': False, 'name': 'xyz00-admin', 'quota_hardlimit': '0', 'userid': '104225', 'quota_softlimit': '0', 'pac': 'xyz00', 'id': '12184', 'homedir': '/home/pacs/xyz00/users/admin'}]
>>>
>>> api.user.update(where={'name': 'xyz00-admin'}, set={'password': 'less-secret'})
>>>
>>> api.domain.add(set={'name': 'example.com', user: 'xyz00-admin'})
>>>
>>> api.domain.delete(where={'name': 'example.com'})
