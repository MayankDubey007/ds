# This is the CircularQueue class
class CircularQueue:
  
  # constructor forz10
  # the class
  # taking input for the size of the Circular queue 
  # from user
  def __init__(self, maxSize):
    self.queue = list()
    # user input value for maxSize
    self.maxSize = maxSize
    self.head = 0
    self.tail = 0

  # add element to the queue
  def enqueue(self, data):
    print("ENQUEUE")
    # if queue is full
    if self.size() == (self.maxSize - 1):
        print("if queue is full")
        print(f"self.size(){self.size()} == (self.maxSize - 1){self.maxSize - 1}")
        # return("Queue is full!")
    else:
      print(f"[ELSE]self.size(){self.size()}, (self.maxSize - 1){self.maxSize - 1}")
      # add element to the queue
      self.queue.append(data)
      # increment the tail pointer
      print(f" self.tail = {self.tail}")
      print(f" self.head = {self.head}")
      print(f" queue = {self.queue}")
      
      self.tail = (self.tail+1) % self.maxSize
      print(f" +++ self.tail = {self.tail}")
      return True
  
  # remove element from the queue
  def dequeue(self):
    print("DEQUEUE")
    # if queue is empty
    if self.size() == 0:
      print(f"SIZE = {self.size()}")
      return("Queue is empty!")
    else:
      # fetch data
      
      print(f"SIZE = {self.size()}")
      print(f"prnt = {self.queue}")
      print(f"data = {self.queue[self.head]} = HEAD = {self.head}")
      data = self.queue[self.head]
      # increment head
      print(f"HEAD = {self.head}")
      self.head = (self.head+1) % self.maxSize
      print(f"aft op HEAD = {self.head}")
      return data
  
  # find the size of the queue
  def size(self):
    print(f"(1)def-> \t self.tail = {self.tail} and self.head = {self.head}")
    if self.tail >= self.head:
      print(f"(2)IF-> \t qSIZE ({self.tail - self.head}) = {self.tail} - {self.head}")
      qSize = self.tail - self.head
    else:
      print(f"(3)ELSE-> \t self.tail = {self.tail} and self.head = {self.head}")
      qSize = self.maxSize - (self.head - self.tail)
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