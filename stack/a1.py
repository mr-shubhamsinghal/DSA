
"""
Implement Stack using two queues

Push - O(n)
Pop - O(1)
"""

class Queue:

    def __init__(self):
        self.queue = []
        self.front = -1
        self.rear = -1

    def get_front(self):
        return self.front
    
    def get_rear(self):
        return self.rear

    def enqueue(self, x):
        if self.front == -1 and self.rear == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear += 1
        self.queue.append(x)
        return

    def dequeue(self):
        if self.front == -1 and self.rear == -1:
            print('queue is empty')
            return
        elif self.front == self.rear:
            popped_element = self.queue.pop(0)
            self.front = -1
            self.rear = -1
        else:
            popped_element = self.queue.pop(self.front)
            self.front += 1
        return popped_element

    def display(self):
        if self.front == -1 and self.rear == -1:
            print('queue is empty')
            return
        else:
            for i in range(self.front, self.rear+1):
                print(self.queue[i], end=" ")
            print()

class stack_using_queues(Queue):

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
    
    def push(self, x):
        if self.q1.get_front() == -1:
            self.q1.enqueue(x)
        else:
            while self.q1.get_front() != -1:
                self.q2.enqueue(self.q1.dequeue())
            self.q1.enqueue(x)
            while self.q2.get_front() != -1:
                self.q1.enqueue(self.q2.dequeue())

    def pop(self):
        if self.q1.get_front() == -1 and self.q1.get_rear() == -1:
            print('stack is empty')
        else:
            popped_element = self.q1.dequeue()
            return popped_element

    def display(self):
        self.q1.display()


s = stack_using_queues()
s.push(2)
s.push(3)
s.push(5)
print(s.pop())
s.push(1)
print(s.pop())
print('stack :', s.display())
