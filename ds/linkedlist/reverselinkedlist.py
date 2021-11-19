class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        print("\n")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def length(self):
        cc = 0
        temp = self.head
        print("\n")
        while temp:
            cc += 1
            print(f"{cc} = {temp.data}")
            temp = temp.next

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


obj = DoublyLinkedList()
# obj.reverse()
obj.prepend(1)
obj.prepend(2)
obj.prepend(3)

obj.prepend(4)
obj.print_list()
obj.reverse()
obj.print_list()
obj.length()
