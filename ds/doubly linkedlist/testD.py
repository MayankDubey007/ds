class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Dlist:
    def __init__(self):
        self.head = None
    def printL(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
    def append(self,data):
        temp = self.head
        newnode = Node(data)
        if temp == None:
            # temp = newnode
            self.head = newnode
            # newnode.prev = Node
            newnode.prev = None
        else:
            while temp.next:
                temp = temp.next
            if temp.next == None:
                temp.next = newnode
                newnode.prev = temp
                newnode.next = None
    def prepend(self,data):
        newnode = Node(data)
        temp = self.head
        if self.head == None:
            self.head = newnode
            newnode.next = None
            newnode = None
        else:
            nxt = self.head
            self.head = newnode
            newnode.prev = None
            newnode.next = nxt
            nxt.prev = newnode
    def addafter(self,key,data):
        newnode = Node(data)
        temp = self.head
        while temp:
            if temp.next == None and temp.data == key:
                self.append(data)
            elif temp.data == key:
                nxt = temp.next
                temp.next = newnode
                newnode.prev = temp
                newnode.next = nxt
                nxt.prev = newnode
            temp = temp.next    
                
obj = Dlist()            
obj.append(1)
obj.append(2)
obj.append(3)
obj.append(4)
obj.append(5)
obj.prepend(6)
obj.prepend(7)
obj.prepend(8)
obj.prepend(9)
obj.prepend(101)
obj.addafter(9,12)
obj.printL()