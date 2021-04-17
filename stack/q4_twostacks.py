
"""
Implement two stack in an array
"""

class Stack:
    
    def __init__(self, n):

        self.size = n
        self.stack = [None] * n
        self.top1 = -1
        self.top2 = self.size

    
    def push1(self, item):

        if self.top1 < self.top2 -1:
            self.top1 = self.top1 + 1
            self.stack[self.top1] = item
        else:
            print('stack1 overflow')
            exit(1)

    def push2(self, item):

        if self.top2 - 1 > self.top1:
            self.top2 = self.top2 - 1
            self.stack[self.top2] = item
        else:
            print('stack2 overflow')
            exit(1)

    def pop1(self):

        if self.top1 == -1:
            print('stack1 underflow')
            return

        temp = self.stack[self.top1] 
        self.stack[self.top1] = None
        self.top1 -= 1
        return temp

    def pop2(self):

        if self.top2 == self.size:
            print('stack2 underflow')
            return

        temp = self.stack[self.top2]
        self.stack[self.top2] = None
        self.top2 += 1
        return temp


ts = Stack(5)
ts.push1(5)
ts.push2(10)
ts.push2(15)
ts.push1(11)
ts.push2(7)

print('popped element from stack1 is ' + str(ts.pop1()))
ts.push2(40)
print('popped element from stack2 is ' + str(ts.pop2()))
