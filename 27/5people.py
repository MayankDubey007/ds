class queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,value):
        if self.queue == len(self.queue):
            print("queue is full filed")
        else:
            self.queue.append(value)              
    def dequeue(self):
        if len(self.queue) == 0:
            print("queue is empty")
        else:
            self.queue.pop(0)
    def prnt(self):
        for i in range(len(self.queue)):
            print(self.queue[i],end=",")
        print("\n")
q = queue()
# q.prnt()
print("5 people already added")
q.enqueue("p")
q.enqueue("p")
q.enqueue("p")
q.enqueue("p")
q.enqueue("p")
print("2 got ticket")
q.dequeue()
q.dequeue()
q.prnt()
print("3 friends join ticket")
q.enqueue("f1")
q.enqueue("f2")
q.enqueue("f3")
q.prnt()
print("3 person got ticket")
q.dequeue()
q.dequeue()
q.dequeue()
print("2 girl joined")
q.enqueue("g1")
q.enqueue("g2")

q.prnt()

# q.enqueue(42)
# q.enqueue(88)
# [4]
# [5]
# [6]