# class Descriptor:

#     def __get__(self, instance, type):
#         return instance.__dict__
    
#     def __set__(self, instance, value):
#         instance.__dict__ = value

class D():

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def __getattribute__(self, attr):
        # if attr.startswith("__"):
        return object.__getattribute__(self, attr)
        # return object

d = D('shubham', 24)
print(d.__name)
print(d.__age)

# class Vehicle():
#     can_fly = False
#     number_of_weels = 0

# class Car(Vehicle):
#     number_of_weels = 4

#     def __init__(self, color):
#         self.color = color

# my_car = Car("red")
# print(my_car.__dict__)
# print(type(my_car).__dict__)