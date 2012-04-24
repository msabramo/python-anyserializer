import biplist

from ..serializer import Serializer


class BiplistSerializer(Serializer):

    def __init__(self):
        super(BiplistSerializer, self).__init__()

    def serialize(self, obj, *args, **kwargs):
        return biplist.writePlistToString(obj, *args, **kwargs)
