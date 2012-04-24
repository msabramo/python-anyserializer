python-anyserializer
=========================

.. image:: https://secure.travis-ci.org/msabramo/python-anyserializer.png?branch=master

A uniform interface to a bunch of different ways to serialize data in Python.

There are a plethora of ways to serialize data in Python, but they often have
annoyingly different interfaces.

For example:

- json and pickle - use "dumps"
- yaml (PyYAML) - uses "dump"
- plistlib and biplist - use "writePlistToString"
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
    >>> anyserializer.serialize('plist', {'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4}})
    '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n<plist version="1.0">\n<dict>\n\t<key>a</key>\n\t<integer>1</integer>\n\t<key>b</key>\n\t<integer>2</integer>\n\t<key>c</key>\n\t<dict>\n\t\t<key>d</key>\n\t\t<integer>3</integer>\n\t\t<key>e</key>\n\t\t<integer>4</integer>\n\t</dict>\n</dict>\n</plist>\n'
    >>> anyserializer.serialize('biplist', {'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4}})
    'bplist00bybiplist1.0\x00\xd3\x01\x02\x03\x04\x05\x06QaQcQb\x10\x01\xd2\x07\x08\t\nQeQd\x10\x04\x10\x03\x10\x02\x15\x1c\x1e "$1)+-/\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x003'

