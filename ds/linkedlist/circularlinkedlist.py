
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:

    def __init__(self):
        self.head = None

    def push(self, data):
        newnode = Node(data)
        temp = self.head

        newnode.next = self.head  # difrentline

        # If linked list is not None then set the next of
        # last node
        if self.head is not None:
            while(temp.next != self.head):
                temp = temp.next
            temp.next = newnode  # difrentline

        else:
            newnode.next = newnode  # For the first node

        self.head = newnode  # difrentline

    def pop(self):
        if self.head == None:
            print("linked list is empty")
        else:
            temp = self.head
            self.head = self.head.next

    # Function to print nodes in a given circular linked list
    # def printList(self):
    #     temp = self.head
    #     if self.head is not None:
    #         while(True):
    #             print(temp.data, end=" ")
    #             temp = temp.next
    #             if (temp == self.head):
    #                 break
    def printL(self):
        temp = self.head
        print(f"{temp.data}", end=" ")
        temp = temp.next
        if temp is not self.head:
            while(True):
                print(temp.data, end=" ")
                temp = temp.next
                if (temp == self.head):
                    break


cllist = CircularLinkedList()

# Created linked list will be 11->2->56->12
cllist.push(12)
cllist.push(56)
cllist.push(2)
cllist.push(11)

print("Contents of circular Linked List")
cllist.printL()
cllist.pop()
print("Contents of circular Linked List")
cllist.printL()
# This code is contributed by
# Nikhil Kumar Singh(nickzuck_007)
