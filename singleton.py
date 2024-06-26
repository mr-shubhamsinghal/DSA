
class Singleton(type):

    __instance = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls.__instance:
            cls.__instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instance[cls]

class A(metaclass=Singleton):
    def __init__(self):
        pass

obj = A()
print(obj)
obj1 = A()
print(obj1)