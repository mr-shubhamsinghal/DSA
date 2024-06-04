# class based decorators taking arguments

class MyDecorator:
    def __init__(self, arg):
        self.arg = arg
    
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f"before func call {self.arg}")
            result = func(*args, **kwargs)
            return result
        return wrapper



# Simple class based decorators

# class MyDecorator:
#     def __init__(self, func):
#         self.func = func

#     def __call__(self, *args, **kwargs):
#         print("before calling main func")
#         result = self.func(*args, **kwargs)
#         print("after calling main func")
#         return result

# @MyDecorator
@MyDecorator(1)
def plus_two(a, b):
    return a + b

print(plus_two(1, 2))