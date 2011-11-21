class SerializerFactory(object):

    def __init__(self, registry=None):
        if registry is None:
            registry = {}

        self.registry = registry

    def output_formats(self):
        return self.registry.keys()

    def register(self, output_format, cls):
        self.registry[output_format] = cls

    def get_serializer(self, output_format):
        return self.registry[output_format]()
