from .serializerfactory import SerializerFactory
from .serializers import *


serializer_factory = SerializerFactory({
    'json': JsonSerializer,
    'yaml': YamlSerializer,
    'plist': PlistSerializer,
    'biplist': BiplistSerializer,
    'pprint': PprintSerializer,
    'phpserialize': PhpSerializer,
    'pickle': PickleSerializer,
})

get_serializer = serializer_factory.get_serializer
output_formats = serializer_factory.output_formats

def serialize(output_format, obj):
    return get_serializer(output_format).serialize(obj)
