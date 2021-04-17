
"""
Implement a Queue class (using arrays) with the following methods:

    enqueue()
    dequeue()
    front()
    display()
"""

class Queue:

    def __init__(self, n):
        self.size = n
        self.queue = [None] * n
        self.front = self.rear = -1

    def empty(self):
        return self.front == -1

    def queue_front(self):
        return self.queue[self.front]

    def display(self):
        if self.empty():
            print('queue is empty')
            return
        a = []
        for i in range(self.front, self.rear+1):
            a.append(self.queue[i])
        print(a)

    def enqueue(self, item):
        if self.rear >= self.size-1:
            print('queue is full')
            return
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = item
        else:
            self.rear += 1
            self.queue[self.rear] = item

    def dequeue(self):
        if self.empty():
            print('queue is empty')
            return
        elif self.front == self.rear:
            self.queue[self.front] = None
            self.front = -1
            self.rear = -1
        else:
            self.queue[self.front] = None
            self.front += 1
        return

q = Queue(4)

q.display()

q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

q.display()

q.enqueue(60)

q.display()

q.dequeue()
q.dequeue()

q.display()

print(q.queue_front())
