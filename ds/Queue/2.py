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
            self.head = (self.head+1) % self.maxsize
            return data


Qsize = input("Enter the Qsize of the Circular Queue")
q = circularQueue(int(Qsize))
# q = circularQueue(int(10))

# change the Enqueue and Dequeue statements as you want
print(q.Enqueue(10))
print(q.Enqueue(20))
print(q.Enqueue(30))
print(q.Enqueue(40))
print(q.Enqueue(50))
print(q.Enqueue('Studytonight'))
print(q.Enqueue(70))
print(q.Enqueue(80))
print(q.Enqueue(90))
print(q.Enqueue(100))
print(q.Dequeue())
print(q.Dequeue())
print(q.Dequeue())
print(q.Dequeue())
print(q.Dequeue())
print(q.Dequeue())
print(q.Dequeue())
print(q.Dequeue())
print(q.Dequeue())
