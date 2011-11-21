from ..serializer import Serializer


class YamlSerializer(Serializer):

    def __init__(self):
        super(YamlSerializer, self).__init__()
        import yaml
        self.yaml = yaml

    def serialize(self, obj, *args, **kwargs):
        return self.yaml.dump(obj, *args, **kwargs)
