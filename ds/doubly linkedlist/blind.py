class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
class linkedlist:
    def __init__(self):
        self.head = None
    def addStart(self,data):
        self.head = Node(data=data)
    def trav(self):
        temp = self.head
        cc = 0
        while temp:
            cc+=1
            print(temp)
            temp = temp.next
    def deleteend(self):
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None     
    
obj = linkedlist()            
obj.addStart(1)
obj.addStart(2)
obj.addStart(3)
obj.addStart(4)
obj.addStart(5)
obj.addStart(6)
obj.addStart(7)
obj.addStart(8)
obj.addStart(9)
obj.trav()