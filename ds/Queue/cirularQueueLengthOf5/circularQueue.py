class circularQueue:
    def Qsize(self):
        if self.tail >= self.head:
            Qsize = self.tail - self.head
        else:
            Qsize = self.maxsize - (self.head - self.tail)
            return Qsize

    def __init__(self, maxsize):
        self.queue = list()
        self.maxsize = maxsize
        self.head = 0
        self.tail = 0

    def Enqueue(self, data):
        if self.Qsize() == (self.maxsize - 1):
            return("Queue is full")
        else:
            self.queue.append(data)
            self.tail = (self.tail+1) % self.maxsize
            return True

    def Dequeue(self):
        if self.Qsize() == 0:
            return("Queue is Empty")
        else:
            data = self.queue[self.head]
            self.queue.pop(0)
            self.head = (self.head+1) % self.maxsize
            return data

    def prtnQ(self):
        print(self.queue)


Qsize = input("Enter the Qsize of the Circular Queue")
q = circularQueue(int(Qsize)+1)
print("[1] insert (12,34,56)")
print(q.Enqueue(12))
print(q.Enqueue(34))
print(q.Enqueue(56))
print("[2] Remove 1 element ")
print(q.Dequeue())
print("[3] insert (45,67,89)")
print(q.Enqueue(45))
print(q.Enqueue(67))
print(q.Enqueue(89))
print("[2] Remove 1 element ")
print(q.Dequeue())
print(q.Dequeue())
q.prtnQ()
