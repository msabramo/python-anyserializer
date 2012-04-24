from ..serializer import Serializer


class BsonSerializer(Serializer):

    def __init__(self):
        super(BsonSerializer, self).__init__()
        import bson
        self.bson = bson

    def serialize(self, obj, *args, **kwargs):
        return self.bson.dumps(obj, *args, **kwargs)
