
class Stack:
    
    def __init__(self):
        
        self.stack = []
        self.top = -1

    def empty(self):
        
        return self.top == -1

    def push(self, item):
        self.top += 1
        self.stack.append(item)

    def pop(self):
        
        if self.empty(): return
        self.top -= 1
        return self.stack.pop()

def check_exp_balance_parentheses(expr):

    stack = Stack()
    for char in expr:
        if char in ['(', '[', '{']:
            stack.push(char)
        else:
            if stack.empty():
                return False
            curr_char = stack.pop()
            if curr_char == '(':
                if char != ')':
                    return False
            if curr_char == '[':
                if char != ']':
                    return False
            if curr_char == '{':
                if char != '}':
                    return False
    if stack.stack:
        return False
    return True



exp = '[()]{}{[()()]()}'
balanced = check_exp_balance_parentheses(exp)
print('balanced ', balanced)
