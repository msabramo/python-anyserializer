from ..serializer import Serializer


class BiplistSerializer(Serializer):

    def __init__(self):
        super(BiplistSerializer, self).__init__()
        import biplist
        self.biplist = biplist

    def serialize(self, obj, *args, **kwargs):
        return self.biplist.writePlistToString(obj, *args, **kwargs)
