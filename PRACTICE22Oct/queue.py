class Queue:
    def __init__(self,maxsize):
        self.queue = []
        self.maxsize = maxsize
    def  enqueue(self,Data):
        if len(self.queue) == self.maxsize:
            print("Queue is full filled")
        else:
            self.queue.append(Data)
            print(f"enQueue Data = {Data}")
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue Element is empty")
        else:
            print(f"deQueue Data = {self.queue.pop(0)}")
    def print(self):
        ln = len(self.queue)
        for i in range(0,ln):
            print(self.queue[i],end=",")
        print()
        print(f"first Element = {self.queue[0]}")
        print(f"last Element = {self.queue[-1]}")
Q = Queue(8)
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(4)
Q.enqueue(5)
Q.enqueue(6)
Q.enqueue(7)
Q.enqueue(8)
Q.print()
Q.dequeue()
Q.dequeue()
Q.dequeue()
Q.dequeue()
Q.dequeue()
Q.dequeue()
Q.dequeue()
Q.dequeue()