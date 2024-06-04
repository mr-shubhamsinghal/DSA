class Base:

    _fields = []

    def __init__(self, *args, **kwargs):
        for name, value in zip(self._fields, args):
            print(name, " = ", value)
            setattr(self, name, value)


class Person(Base):

    _fields = ["name", "age"]

    def methodA(self):
        print("Ok Name is {}".format(self.name))

p = Person("shubham", 25)
p.methodA()