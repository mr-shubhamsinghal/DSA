

def second_program(func):
    def wrapper(*args, **kwargs):
        print("called wrapper")
        return func(*args, **kwargs)
    return wrapper

@second_program
def first_program(a, b):
    print("first program")
    return a, b

# a = second_program
# b = 


print(first_program(1, 2))
