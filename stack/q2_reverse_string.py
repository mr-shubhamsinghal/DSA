
"""
Reverse a String using Stack
"""

def create_stack():
    stack = []
    return stack

def size(stack):
    return len(stack)

def isEmpty(stack):
    return size(stack) == 0

def push(stack, item):
    stack.append(item)

def pop(stack):
    if isEmpty(stack): return
    return stack.pop()

def reverse_string(string):

    n = len(string)
    stack = create_stack()
    for i in range(0, n):
        push(stack, string[i])

    string = ''
    for i in range(0, n):
        string += pop(stack)

    return string

string = 'GeeksQuiz'
string = reverse_string(string)
print('reversed string is :', string)

    

