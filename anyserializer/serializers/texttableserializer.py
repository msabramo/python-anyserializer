from ..serializer import Serializer


class TextTableSerializer(Serializer):

    def __init__(self):
        super(TextTableSerializer, self).__init__()
        import texttable
        self.table = texttable.Texttable(max_width=0)
        self.table.set_deco(texttable.Texttable.HEADER)

    def serialize(self, obj, *args, **kwargs):
        if 'header_fields' in kwargs:
            self.table.header(kwargs['header_fields'])

        for row in sorted(obj.items()):
            self.table.add_row(row)

        return self.table.draw()
