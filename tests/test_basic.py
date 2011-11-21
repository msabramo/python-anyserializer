import anyserializer
import pickle
import pytest


a_dict = {'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4}}

expected_json = '{"a": 1, "c": {"e": 4, "d": 3}, "b": 2}'

expected_yaml = """
a: 1
b: 2
c: {d: 3, e: 4}
"""

expected_pprint = "{'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4}}"

expected_phpserialize = b'a:3:{s:1:"a";i:1;s:1:"c";a:2:{s:1:"e";i:4;s:1:"d";i:3;}s:1:"b";i:2;}'


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


def test_serialize_to_unknown_format():
    with pytest.raises(KeyError):
        output = anyserializer.serialize('foobar', a_dict)
