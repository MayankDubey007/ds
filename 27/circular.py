class Q:
    def __init__(self,max):
        self.queue = []
        self.max = max
        self.tail = 0
        self.head = 0
    def enQueue(self,value):
        if len(self.queue) == self.max:
            p("Queue is  fully filled")
        else:
            self.queue.append(value)
            self.tail  = (self.tail + 1) % self.max
            return True
    def deQueue(self):
        if self.SZ() == 0:
            ret("element not present in Queue")
        else:
            # value = self.queue.pop(0)
            # ya
            valu = self.queue[self.head]
            self.head = (self.head + 1) % self.max
        return valu
    
    def SZ(self):
        if self.tail >= self.head:
            Qsz = self.tail - self.head
        else:
            Qsz = self.max - (self.head - self.tail)
        return Qsz
    def display(self):
        for i in range(len(self.queue)):
            print(self.queue[i],end=",")
        print()
        
        
q = Q(7)
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)
q.enQueue(4)
q.enQueue(5)
q.enQueue(6)
q.enQueue(7)
q.enQueue(8)
q.display()
print(q.SZ())
q.deQueue()
q.deQueue()
q.deQueue()
q.deQueue()
q.deQueue()
q.deQueue()
q.deQueue()
q.deQueue()
q.deQueue()
q.display()