class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linklist:
    def __init__(self):
        self.head = None

    def viewList(self):
        if self.head == None:
            print("list is empty")
        else:
            temp = self.head
            while temp != None:
                print(temp.data, end="  ")
                temp=temp.next

    def deQueue(self):
        if self.head == None:
            print("linked list is empty")
        else:
            temp = self.head
            self.head = self.head.next

    def denQueue(self, value):
        newnode = node(value)
        if (self.head == None):
            self.head = newnode
        else:
            temp = self.head
            while (temp.next != None):
                temp = temp.next
            temp.next = newnode


mylist = linklist()
mylist.denQueue(10)
mylist.denQueue(20)
mylist.denQueue(30)
mylist.denQueue(40)
mylist.denQueue(50)
mylist.denQueue(60)
mylist.denQueue(70)
mylist.denQueue(80)
mylist.denQueue(90)
mylist.viewList()
mylist.deQueue()
mylist.deQueue()
mylist.deQueue()
mylist.deQueue()
print()
mylist.viewList()
