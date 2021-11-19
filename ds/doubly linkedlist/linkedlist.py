class Node:
    def __init__(self,data= None,next=None):
        self.data = data
        self.next = next
class Linked_List:
    def __init__(self):
        self.head = None
    def traverse(self):  # 321
        temp = self.head
        while temp:
            print(temp.data,'->', end= ' ')
            temp = temp.next
        print(temp)
    def addstart(self,data):
        if self.head is None:
            
    def addend(self,data):
        New_Node = Node(data=data)
        if(self.head == None):
            self.head = New_Node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = New_Node
    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        print("Linked List Length = {}".format(count))
    def poss(self,pos):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
            if (pos == count):
                print(f"if pos = {pos} then data = {temp.data}")
    def addgivenpos(self,data,pos):
        New_Node = Node(data=data)
        if(self.head == None):
            print("Linked List Is Empty...")
        elif(pos == 0):
            ob1.addstart(data)
        else:
            temp = self.head
            cc = -1
            while temp:
                if(cc == pos-2):
                    tt = temp.next
                    temp.next = New_Node
                    New_Node.next = tt
                else:
                    temp = temp.next
                cc += 1
    def addgivenpos2(self,data,pos):
        New_Node = Node(data=data)
        if(self.head == None):
            print("Linked List Is Empty...")
        elif(pos == 0):
            ob1.addstart(data)
        else:
            temp = self.head
            cc = 0
            while temp:
                if(cc == pos-1):
                    tt = temp.next
                    temp.next = New_Node
                    New_Node.next = tt
                else:
                    temp = temp.next
                cc += 1
    def deletestart(self):
        if(self.head == None):
            print("Linked List Is Empty So Deletion is Not Possible...")
        else: 
            self.head = self.head.next
    def deleteend(self):
        if(self.head == None):
            print("Linked List Is Empty So Deletion is Not Possible...")
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            temp.next = None
    def emptylinkedlist(self):
        self.head = None
ob1 = Linked_List()
ob1.addend(1)
ob1.addend(2)
ob1.addend(3)
ob1.addend(4)
ob1.addend(5)
ob1.addend(6)
ob1.addend(77)
ob1.poss(5)
ob1.traverse()
# ob1.addgivenpos(5,5)
# ob1.traverse()
