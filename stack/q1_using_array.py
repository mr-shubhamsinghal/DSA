
"""
Implement a Stack Class with the following methods:
    push()
    pop()
    peek()
    empty()
    search()
"""

class Stack:
    def __init__(self, size):
        self.stack = [None] * size
        self.size = size
        self.top = -1

    def empty(self):
        return self.top == -1

    def full(self):
        return self.top+1 == self.size

    def push(self, item):
        if self.full():
            return 'stack is full'
        self.top += 1
        self.stack[self.top] = item

    def pop(self):
        if self.empty():
            return 'stack is empty'
        popped_data = self.peek()
        self.stack[self.top] = None
        self.top -= 1
        return popped_data
    
    def peek(self):
        if self.empty():
            return 'stack is empty'
        return self.stack[self.top]

    def search(self, item):
        if self.empty():
            return 'stack is empty'
        for i in range(self.top+1):
            if item == self.stack[i]:
                return 'True'
        return 'False'


stack = Stack(5)

print('peek ', stack.peek())
stack.push(10)
print('peek ',stack.peek())
stack.push(20)
print('peek ',stack.peek())
stack.push(30)
print('search ',stack.search(30))
print('popped element ',stack.pop())
print('peek element ',stack.peek())
print('searched element ',stack.search(10))
print('searched element ',stack.search(30))
