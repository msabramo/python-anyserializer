import plistlib

from ..serializer import Serializer


class PlistSerializer(Serializer):

    def __init__(self):
        super(PlistSerializer, self).__init__()

    def serialize(self, obj, *args, **kwargs):
        return plistlib.writePlistToString(obj, *args, **kwargs)
