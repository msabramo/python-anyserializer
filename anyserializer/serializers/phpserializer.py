from ..serializer import Serializer


class PhpSerializer(Serializer):

    def __init__(self):
        super(PhpSerializer, self).__init__()
        import phpserialize
        self.phpserialize = phpserialize

    def serialize(self, obj, *args, **kwargs):
        return self.phpserialize.dumps(obj, *args, **kwargs)
