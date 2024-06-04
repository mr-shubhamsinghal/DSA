








class Foo:
    def __init__(self, name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

# Descriptor version of above
        



if __name__ == "__main__":
    f = Foo('shubham')
    print(f)
    print(f.name)
    f.name = 'ankit'
    print(f.name)