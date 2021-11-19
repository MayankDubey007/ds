class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self):
        self.head = None
    def addstart(self,data):
        self.head = Node(data=data,next=self.head)
    def addend(self,data):
        Nnode = Node(data=data)
        if (self.head==None):
            print("Linked List is empty")
        else:
            temp = self.head
            while temp:
                temp = temp.next
            temp.data = data
    def addpos(self,data,pos):
        nNode = Node(data=data)
        if(self.head == None):
            print("linkedList is Empty")
        elif(pos == 0):
            obj.addstart(data)
        else:
            cc = 0
            temp = self.head
            while temp:
                if(cc == pos-1):
                    tt = temp.next
                    temp.next = nNode
                    nNode = tt
                else:
                    temp = temp.next
                cc+=1
    def delStart(self):
        if(self.head == None):
            print("deletion not posible")
        else:
            self.head = self.head.next
    def delEnd(self):
        if(self.head == None):
            print("deletion not posible")
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            temp.next = None

    def traversel(self):
        temp = self.head
        while temp:
            print(temp.data,"->",end=" ")
            temp = temp.next
        print(temp)
        
        # break

obj = linkedlist()
obj.addstart(1)
obj.addstart(2)
obj.addstart(3)
obj.addstart(4)
obj.addstart(5)
obj.addstart(6)
obj.addstart(7)
obj.addstart(8)
obj.addstart(9)
obj.addpos(12,4)
obj.traversel()
obj.delEnd()
obj.delEnd()
obj.traversel()
# print(obj.delStart())