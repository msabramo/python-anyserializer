from ..serializer import Serializer


class PickleSerializer(Serializer):

    def __init__(self):
        super(PickleSerializer, self).__init__()
        self.pickle = self._import_pickle()

    def serialize(self, obj, *args, **kwargs):
        return self.pickle.dumps(obj, *args, **kwargs)

    @staticmethod
    def _import_pickle():
        """Import a module for pickle"""

        try:
            import cPickle as pickle
        except ImportError:
            import pickle

        return pickle
