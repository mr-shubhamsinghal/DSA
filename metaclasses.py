
class D(type):
    def __call__(cls, *args, **kwargs):
        instance = super(D, cls).__call__(*args, **kwargs)
        return instance
    
    def __init__(cls, *args, **kwargs):
        super(D, cls).__init__(*args, **kwargs)

class E(metaclass=D):
    pass

e = E()
print(e)
    
