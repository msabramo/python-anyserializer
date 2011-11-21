from ..serializer import Serializer


class PprintSerializer(Serializer):

    def __init__(self):
        super(PprintSerializer, self).__init__()
        from pprint import pformat
        self.pformat = pformat

    def serialize(self, obj, *args, **kwargs):
        return self.pformat(obj, *args, **kwargs)
