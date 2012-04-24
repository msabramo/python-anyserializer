import pickle
import sys

import pytest

import anyserializer


a_dict = {'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4}}

expected_json = '{"a": 1, "c": {"e": 4, "d": 3}, "b": 2}'

expected_yaml = """
a: 1
b: 2
c: {d: 3, e: 4}
"""

expected_pprint = "{'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4}}"

expected_phpserialize = b'a:3:{s:1:"a";i:1;s:1:"c";a:2:{s:1:"e";i:4;s:1:"d";i:3;}s:1:"b";i:2;}'

expected_plist = """
<plist version="1.0">
<dict>
	<key>a</key>
	<integer>1</integer>
	<key>b</key>
	<integer>2</integer>
	<key>c</key>
	<dict>
		<key>d</key>
		<integer>3</integer>
		<key>e</key>
		<integer>4</integer>
	</dict>
</dict>
</plist>
"""

if sys.version_info[0] >= 3:
    expected_plist = expected_plist.encode('utf-8')

expected_biplist = 'bplist00bybiplist1.0\x00\xd3\x01\x02\x03\x04\x05\x06QaQcQb\x10\x01\xd2\x07\x08\t\nQeQd\x10\x04\x10\x03\x10\x02\x15\x1c\x1e "$1)+-/\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x003'


def test_serialize_to_json():
    output = anyserializer.serialize('json', a_dict)
    assert output.strip() == expected_json.strip()


def test_serialize_to_yaml():
    output = anyserializer.serialize('yaml', a_dict)
    assert output.strip() == expected_yaml.strip()


def test_serialize_to_pprint():
    output = anyserializer.serialize('pprint', a_dict)
    assert output.strip() == expected_pprint.strip()


def test_serialize_to_pickle():
    output = anyserializer.serialize('pickle', a_dict)
    b_dict = pickle.loads(output)
    assert a_dict == b_dict


def test_serialize_to_phpserialize():
    output = anyserializer.serialize('phpserialize', a_dict)
    assert output.strip() == expected_phpserialize.strip()


def test_serialize_to_plist():
    output = anyserializer.serialize('plist', a_dict)
    assert expected_plist.strip() in output.strip()


# def test_serialize_to_biplist():
#     output = anyserializer.serialize('biplist', a_dict)
#     assert output.strip() == expected_biplist.strip()


def test_serialize_to_unknown_format():
    with pytest.raises(KeyError):
        output = anyserializer.serialize('foobar', a_dict)
