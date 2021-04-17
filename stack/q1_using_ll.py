
"""
Implement a Stack Class with the following methods:
    push()
    pop()
    peek()
    empty()
    search()
"""

class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def empty(self):
        return self.top == None

    def push(self, item):
        new_node = node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.empty():
            return 'stack is empty'
        temp = self.top
        self.top = self.top.next
        return temp.data

    def peek(self):
        if self.empty():
            return 'stack is empty'
        return self.top.data

    def search(self, item):
        if self.empty():
            return 'stack is empty'
        node = self.top
        while node:
            if node.data == item:
                return 'True'
            node = node.next
        return 'False'

stack = Stack()

print('search :', stack.search(10))

stack.push(10)
stack.push(20)
stack.push(30)

print('search :', stack.search(10))
print('peek :', stack.peek())
print('pop :', stack.pop())
print('peek :', stack.peek())
