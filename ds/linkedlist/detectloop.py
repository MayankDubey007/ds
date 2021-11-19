class Node:

	def __init__(self, data):
		self.data = data
		self.next = None
class LinkedList:

	def __init__(self):
		self.head = None

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	# Utility function to print it the linked LinkedList
	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data)
			temp = temp.next

	def detectLoop(self):
		slow_p = self.head
		fast_p = self.head
		while(slow_p and fast_p and fast_p.next):
			slow_p = slow_p.next
			fast_p = fast_p.next.next
			if slow_p == fast_p:
				return


# Driver program for testing
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)
llist.push(56)
llist.push(61)
llist.printList()

# Create a loop for testing
head.next.next.next.next.next = head.next.next
if(llist.detectLoop()):
	print("Found Loop")
else:
	print("No Loop")

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
