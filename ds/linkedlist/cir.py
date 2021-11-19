class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def Add(self, val):
        new_node = Node(val)
        runner = self.head
        
        new_node.next = self.head # difrentline
        if self.head is not None:
            while runner.next != self.head:
                runner = runner.next
            runner.next = new_node
        else:
            new_node.next = new_node # difrentline
        self.head = new_node # difrentline
        
        return self
    def Remove(self):
        self.head = self.head.next
        return self

    def remove_from_back(self):
        last_node = self.head
        while last_node.next.next != None:
            last_node = last_node.next
        last_node.next = None
        return self

    # Function to print nodes in a given circular linked list
    # def printList(self):
    #     temp = self.value
    #     if self.value is not None:
    #         while(True):
    #             print(temp.data, end=" ")
    #             temp = temp.next
    #             if (temp == self.value):
    #                 break
    def printL(self):
        temp = self.head
        print(f"{temp.value}", end=" ")
        temp = temp.next
        if temp is not self.head:
            while(True):
                print(temp.value, end=" ")
                temp = temp.next
                if (temp == self.head):
                    break
    def print_values(self):
        runner = self.head
        while runner != None:
            print(runner.value)
            runner = runner.next
        return self


cllist = CircularLinkedList()

# Created linked list will be 11->2->56->12
cllist.add_to_front("10")
cllist.add_to_front("20")
cllist.add_to_front("30")
cllist.add_to_front("40")
cllist.add_to_front("50")
cllist.add_to_front("60")
cllist.add_to_front("70")

print("Contents of circular Linked List")
cllist.printL()
print("Contents of circular Linked List")
# This code is contributed by
# Nikhil Kumar Singh(nickzuck_007)
