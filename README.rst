python-anyserializer
=========================

.. image:: https://secure.travis-ci.org/msabramo/python-anyserializer.png?branch=master

A uniform interface to a bunch of different ways to serialize data in Python.

There are a plethora of ways to serialize data in Python, but they often have
annoyingly different interfaces.

For example:

- JSON - uses "dumps"
- YAML - uses "dump"
- etc.

This makes it a bit annoying when you're writing software and want to be able
to let the user specify different serialization formats.

Some frameworks have developed useful abstractions for serialization. For
example, `Django's serialization framework
<https://docs.djangoproject.com/en/dev/topics/serialization/>`_. But this is
unnecessarily tied to the Django framework and the Django ORM. Serialization is
a general problem that is not specific to any framework.

Things shouldn't be this way.

::

    >>> anyserializer.serialize('json', {'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4}})
    '{"a": 1, "c": {"e": 4, "d": 3}, "b": 2}'
    >>> anyserializer.serialize('yaml', {'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4}})
    'a: 1\nb: 2\nc: {d: 3, e: 4}\n'
    >>> anyserializer.serialize('pickle', {'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4}})
    "(dp1\nS'a'\nI1\nsS'c'\n(dp2\nS'e'\nI4\nsS'd'\nI3\nssS'b'\nI2\ns."
    >>> anyserializer.serialize('phpserialize', {'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4}})
    'a:3:{s:1:"a";i:1;s:1:"c";a:2:{s:1:"e";i:4;s:1:"d";i:3;}s:1:"b";i:2;}'

