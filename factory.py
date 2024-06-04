class A:
    def print(self):
        print('A')

class B:
    def print(self):
        print("B")

def get(obj=""):
    objs = dict(a=A(), b=B())
    return objs[obj]

a = get("a")
b = get("b")
a.print()
b.print()