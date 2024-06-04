
class A:
    __slots__ = ('name',)

    def __init__(self, name):
        self.name = name

a = A("ahmed")
print(a.name)
b = A('dsfi')
b.tata = 2
# print(b.tata)