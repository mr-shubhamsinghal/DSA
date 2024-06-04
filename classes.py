class A(object):
    def __call__(cls, *args, **kwargs):
        print('call method')
        return super(A, cls).__call__(cls, *args, **kwargs)
    
    # def __new__(cls, *args, **kwargs):
    #     print("new method")
    #     return super(A, cls).__new__(cls, *args, **kwargs)
    
    # def __init__(self, *args, **kwargs):
    #     print('init method')
    #     return super(A, self).__init__(*args, **kwargs)
    
    def __str__(self):
        return 'A class'
    
    def __repr__(self):
        return 'A is a base class'
    
a = A()
print(a())
