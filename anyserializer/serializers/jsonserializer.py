from ..serializer import Serializer


class JsonSerializer(Serializer):

    def __init__(self):
        super(JsonSerializer, self).__init__()
        self.json = self._import_json()

    def serialize(self, obj, *args, **kwargs):
        return self.json.dumps(obj, *args, **kwargs)

    @staticmethod
    def _import_json():
        """Import a module for JSON"""

        try:
            import json
        except ImportError:
            import simplejson as json
        else:
            return json
