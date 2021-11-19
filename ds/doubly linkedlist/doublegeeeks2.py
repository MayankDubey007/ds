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
        new_node = Node(data)
        if self.head is None:
            new_node.prev = None
            self.head = new_node
        else:
            temp = self.head
            while temp.next:         #ltn
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
            new_node.next = None

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.prev = None 
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def print_list(self):
        temp = self.head
        print("\n")
        while temp:
            print(temp.data,end= " ")
            temp = temp.next
            
    def add_after_node(self, key, data):
        temp = self.head
        while temp:
            if temp.next is None and temp.data == key:
                self.append(data)
                return
            elif temp.data == key:
                new_node = Node(data)
                nxt = temp.next
                temp.next = new_node
                new_node.next = nxt
                new_node.prev = temp
                nxt.prev = new_node
            temp = temp.next

    def add_before_node(self, key, data):
        temp = self.head
        while temp:
            new_node = Node(data)
            if temp.prev is None and temp.data == key:
                self.prepend(data)
                return
            elif temp.data == key:
                prev = temp.prev
                prev.next = new_node
                temp.prev = new_node
                new_node.next = temp
                new_node.prev = prev
            temp = temp.next

    def delete(self, key):
        temp = self.head
        if temp.data == key and temp == self.head:
            # Case 1:#from strating list and only one node in list
            if not temp.next:
                temp = None 
                self.head = None
                return
            # Case 2:#from strating list with many node in list
            else:
                nxt = temp.next
                temp.next = None 
                nxt.prev = None
                temp = None
                self.head = nxt
                return 

        while temp:
            if temp.data == key:
                # Case 3:#delte node from center 
                if temp.next:
                    nxt = temp.next 
                    prev = temp.prev
                    prev.next = nxt
                    nxt.prev = prev
                    temp.next = None 
                    temp.prev = None
                    temp = None
                    return

                # Case 4:#delte node from last 
                elif temp.next is None:
                    prev = temp.prev 
                    prev.next = None 
                    temp.prev = None 
                    temp = None 
                    return 
            temp = temp.next

    def detectLoop(self):
        slow_p = self.head
		fast_p = self.head
		while(slow_p and fast_p and fast_p.next):
			slow_p = slow_p.next
			fast_p = fast_p.next.next
			if slow_p == fast_p:
                print(slow_p)
                print(fast_p)
				return

    def reverse(self):
        tmp = None
        temp = self.head
        while temp:
            tmp = temp.prev
            temp.prev = temp.next
            temp.next = tmp
            temp = temp.prev
        if tmp:
            self.head = tmp.prev

    def remove_duplicates(self):
        temp = self.head 
        seen = dict()
        while temp:
            if temp.data not in seen:
                seen[temp.data] = 1
                temp = temp.next
            else:
                nxt = temp.next
                self.delete_node(temp)
                temp = nxt



obj = DoublyLinkedList()
# # obj.remove_duplicates(self):
# # obj.reverse(self):
# obj.delete_node(self, node):
# # obj.delete(self, key):
# obj.delete(self, key):
# # obj.prepend(self, data):
# obj.prepend(1)
# obj.prepend(2)
# obj.prepend(3)
# obj.prepend(4)
# obj.prepend(5)
# obj.prepend(self, data):
obj.append(1)
obj.append(2)
obj.append(3)
obj.append(4)
obj.append(5)
# obj.append(self, data):
# # obj.print_list(self):
obj.remove_duplicates()
obj.print_list()
obj.reverse()
# obj.print_list()
# obj.delete_node()
# obj.print_list()
# # obj.add_after_node(self, key, data):
# obj.add_after_node(5,11)
# # obj.add_before_node(self, key, data):
# obj.add_before_node(3,333)
obj.print_list()
obj.delete(5)
obj.print_list()