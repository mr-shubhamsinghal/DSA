
"""
Implement a Circular queue with the same methods in the above problem statement

    enqueue()
    dequeue()
    front()
    display()
"""

class Queue:

    def __init__(self, n):
        self.size = n
        self.queue = [None]*n
        self.front = self.rear = -1

    def empty(self):
        return self.front == -1

    def queue_front(self):
        return self.queue[self.front]

    def display(self):
        if self.empty():
            print('queue is empty')
            return
        elif self.front <= self.rear:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.front):
                print(self.queue[i], end=" ")
    
    def enqueue(self, x):
        if (self.rear + 1)%self.size == self.front:
            print('queue is full')
            return
        elif self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1)%self.size
        self.queue[self.rear] = x
        return

    def dequeue(self):
        if self.empty():
            print('queue is empty')
        elif self.front == self.rear:
            self.queue[self.front] = None
            self.front = -1
            self.rear = -1
        else:
            self.queue[self.front] = None
            self.front = (self.front + 1)%self.size
        return

q = Queue(5)

q.enqueue(14)
q.enqueue(22)
q.enqueue(13)
q.enqueue(-6)
q.display()
q.dequeue()
q.dequeue()
q.display()
q.enqueue(9)
q.enqueue(20)
q.enqueue(5)
q.display()
