class Queue:

    def __init__(self, size):
        self.queue = []
        self.size = size

    def enqueue(self, data):
        if len(self.queue)-1 == (self.size - 1):
            print("Queue is full!")
        else:
            self.queue.append(data)
            print(f"enQueue data = {data}")
            return data

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print(f"poped element : {self.queue.pop(0)}")

    def print(self):
        ln = len(self.queue)
        for i in range(ln):
            print(self.queue[i], end=",")
        print(
            f"\nfirst element = {self.queue[0]} And last element = {self.queue[-1]}")


if __name__ == '__main__':
    queue = Queue(6)

    # adding the queue
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)

    queue.dequeue()
    queue.dequeue()
    queue.print()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
