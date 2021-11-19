# This is the CircularQueue class
class CircularQueue:

    # constructor for the class
    # taking input for the size of the Circular queue
    # from user
    def __init__(self, maxSize):
        self.queue = []
        # user input value for maxSize
        self.maxSize = maxSize
        self.head = 0
        self.back = 0

    # add element to the queue
    def enqueue(self, data):
        # if queue is full
        if self.size() == (self.maxsize - 1):
            return("Queue is full!")
        else:
            # add element to the queue
            self.queue.append(data)
            # increment the back pointer

            self.back = (self.back+1) % self.maxSize
            return True

    # remove element from the queue
    def dequeue(self):
        # if queue is empty
        if self.size() == 0:
            return("Queue is empty!")
        else:
            # fetch data
            data = self.queue[self.head]
            # increment head
            self.head = (self.head+1) % self.maxSize
            return data

    # find the size of the queue
    def size(self):
        if self.back >= self.head:
            qSize = self.back - self.head
        else:
            qSize = self.maxSize - (self.head - self.back)
        # return the size of the queue
        return qSize


# input 7 for the size or anything else
size = input("Enter the size of the Circular Queue")
q = CircularQueue(int(size))

# change the enqueue and dequeue statements as you want
print(q.enqueue(10))
print(q.enqueue(20))
print(q.enqueue(30))
print(q.enqueue(40))
print(q.enqueue(50))
print(q.enqueue('Studytonight'))
print(q.enqueue(70))
print(q.enqueue(80))
print(q.enqueue(90))
print(q.enqueue(100))
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
