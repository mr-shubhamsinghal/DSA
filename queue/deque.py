
"""
 Deque
"""

class Deque:

    def __init__(self, n):
        self.size = n
        self.deque = [None]*n
        self.front = -1
        self.rear = -1

    def enqueue_front(self, x):
        if ((self.front == 0 and self.rear == self.size-1) and
                (self.front == self.rear + 1)):
            print('deque is full')
            return
        elif self.front == -1 and self.rear == -1:
            self.front = 0
            self.rear = 0
        elif self.front == 0:
            self.front = self.size-1
        else:
            self.front -= 1
        self.deque[self.front] = x
        return        

    def enqueue_rear(self, x):
        if (self.rear + 1)%self.size == self.front:
            print('deque is full')
            return
        elif self.front == -1 and self.rear == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1)%self.size
        self.deque[self.rear] = x
        return

    def dequeue_front(self):
        if self.front == -1 and self.rear == -1:
            print('deque is empty')
            return
        elif self.front == self.rear:
            self.deque[self.front] = None
            self.front = -1
            self.rear = -1
        else:
            self.deque[self.front] = None
            self.front = (self.front + 1)%self.size
        return

    def dequeue_rear(self):
        if self.front == -1 and self.rear == -1:
            print('deque is empty')
            return
        elif self.front == self.rear:
            self.deque[self.rear] = None
            self.front = -1
            self.rear = -1
        elif self.rear == 0:
            self.deque[self.rear] = None
            self.rear = self.size -1
        else:
            self.deque[self.rear] = None
            self.rear -= 1
        return

    def get_front(self):
        return self.deque[self.front]

    def get_rear(self):
        return self.deque[self.rear]

    def display(self):
        if self.front == -1 and self.rear == -1:
            print('deque is empty')
            return
        else:
            i = self.front
            while i != self.rear:
                print(self.deque[i], end=" ")
                i = (i + 1)%self.size
            print(self.deque[i])
        return


d = Deque(5)
d.enqueue_rear(1)
d.enqueue_rear(2)
d.enqueue_front(3)
d.enqueue_front(4)
d.display()

d.dequeue_rear()
d.dequeue_front()

d.display()
