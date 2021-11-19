# YouTube Video: https://www.youtube.com/watch?v=8kptHdreaTA
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newnode = Node(data=data)
        if self.head is None:
            self.head = newnode
            newnode.prev = None
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newnode
            newnode.prev = temp
    
    
    def prepend(self,data):
        newnode = Node(data=data)
        if self.head is None:
            self.head = newnode
            newnode.prev = None
        else:
            self.head.prev = newnode
            newnode.next = self.head
            newnode.prev = None
            self.head  = newnode
            

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
            
    def addafter(self,key,data):
        newnode = Node(data)
        temp= self.head
        while temp:
            if temp.next is None and temp.data is key:
                self.append(data)
            elif temp.data==key:
                tn = temp.next
                temp.next = newnode
                newnode.next = tn
                newnode.prev = temp
            temp = temp.next
    def addbefore(self, key, data):
        newnode = Node(data)
        temp = self.head
        while temp:
            if temp.prev is None and temp.data is key:
                self.prepend(data)
            elif temp.data is key:
                tp = temp.prev
                temp.prev = newnode
                newnode.next = temp
                newnode.prev .tp
            temp = temp.next
    def delete(self,data)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    # def addbefore(self, key, data):
    #     temp = self.head
    #     new_node = Node(data)
    #     while temp:
    #         if temp.prev is None and temp.data == key:
    #             self.prepend(data)
    #         elif temp.data == key:
    #             prev = temp.prev
    #             prev.next = new_node
    #             temp.prev = new_node
    #             new_node.next = temp
    #             new_node.prev = prev
    #         temp = temp.next

obj = DoublyLinkedList()
obj.prepend(1)
obj.prepend(2)
obj.prepend(3)
obj.prepend(4)
obj.addafter(1,100)
obj.addbefore(4,100)
obj.print_list()

