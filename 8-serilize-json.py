import json


class Contact:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    @property
    def full_name(self):
        return("{} {}".format(self.first, self.last))

class ContactEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Contact):
            return {'is_contact': True,
                    'first': obj.first,
                    'last': obj.last,
                    'full': obj.full_name}
        return super().default(obj)

c = Contact("John", "Smith")
print(json.dumps(c, cls=ContactEncoder))


def decode_contact(dic):
    if dic.get('is_contact'):
        return Contact(dic['first'], dic['last'])
    else:
        return dic

data = ('{"is_contact": true, "last": "smith",'
'"full": "john smith", "first": "john"}')
c = json.loads(data, object_hook=decode_contact)
print(c.fullname)