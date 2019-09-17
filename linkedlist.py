
class Node:
	def __init__(self, value):
		self.value = value
		#sets pointer(next) to none initially
		self.next = None

class LinkedList:
	#When the list if first initialized we have no nodes, so the head is set to none. 
	def __init__(self, head=None):
		self.head = head
		self.size = 0

	def insert_Node(self, value):
		node = Node(value)
		if self.head is None:
			self.head = node
			return
		else:
			currentNode = self.head
			while True:
				if currentNode.next is None:
					currentNode.next = node
					break
				currentNode = currentNode.next

	def print_Linked_List(self):
		currentNode = self.head
		while currentNode is not None:
			print currentNode.value
			currentNode = currentNode.next
		print "None"

'''
#Creates individual Nodes with no connection.
node1 = Node(15)
node2 = Node(68)
node3 = Node(444)
node4 = Node(51)

#Using the next property we can create a relationship between nodes.
node1.next = node2
node2.next = node3
node3.next = node4

currentNode = node1
while True:
	print currentNode.value
	if currentNode.next is None:
		print "None"
		break
	else:
		currentNode = currentNode.next
		print "Current Node is", currentNode
'''

newLL = LinkedList()
newLL.print_Linked_List()
newLL.insert_Node(56)
newLL.print_Linked_List()
newLL.insert_Node(555)
newLL.print_Linked_List()

