"""
Trees are non-linear data structures that organize data in a hierarchal way. 
The Tree data structure is a collection of nodes connected by its edges and may or may not have children.
The first node is always the root and connected to one or more nodes called children. Nodes without children are called leaves.
The height of a tree is the longest path from the root to the deepest leaf. 
The depth of a tree is the number of edges from the root to the node being searched.

BINARY TREES
Binary Trees can have no more than two children.
Contain 3 pieces of data, a node value(int, str, char, etc), a left pointer and a right pointer. 
On any subtree, the left nodes are less than the root node, which is less than all of the right nodes. 

		A
	B 		C

There are three ways to traverse a a tree,
In-Order Traversal A -> B -> C
Pre-Order Traversal B -> A -> C
Post-Order Traversal A -> C -> B
"""

class Node:
	#Left and Right are initially set to none because our node does not have any children.
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	#If we want to add a value that is less than or equal to the current nodes value, we check left. 
	#Otherwise we check values greater to the right.
	def insert(self, value):
		if value <= self.value:
			if self.left == None:
				self.left = Node(value)
			else:
				self.left.insert(value)
		else:
			if self.right == None:
				self.right = Node(value)
			else:
				self.right.insert(value)
	"""
	Checks if value passed is equal to the value of node.
	If so, returns true if not checks to see if value passed is less than value of node.
	If so, checks to see if the value left of node is null if so returns false.
	Otherwise checks recursively the value passed with the value of the left node.
	and if the value passed isn't less than the node it searhes the right side of the tree. 
	"""
	def find(self, value):
		if value == self.value:
			return True
		elif value < self.value:
			if self.left == None:
				return False
			else:
				return self.left.find(value)
		else:
			if self.right == None:
				return False
			else:
				return self.right.find(value)

	"""
	First check to see if the left side of tree is not empty, if we have a left side,
	we recursively call the print method for that side of the tree.
	When we reach the point where the left side is null, we print the value of that node and go back a step to print the root.
	Next we do the first two steps above for the right side of the tree.
	"""
	def printInOrder(self):
		if self.left is not None:
			self.left.printInOrder()
		print(self.value)
		if self.right is not None:
			self.right.printInOrder()

	def printPreorder(self):
		if self.value:
			#First prints data of root node.
			print(self.value)
			#Then recursively checks the and prints the values of the node in the left tree.
			if self.left == None:
				return
			else:
				self.left.printPreorder()
			#Lastly recursively checks the right tree and prints the values of the nodes.
			if self.right == None:
				return
			else:
				self.right.printPreorder()

	def printPostorder(self):
		if self.value:
			#Recursively prints left tree first.
			if self.left is not None:
				self.left.printPostorder()
			else:
				None
			#Next recursively prints right tree second.
			if self.right is not None:
				self.right.printPostorder()
			else:
				None
			#Prints root node last.
			print(self.value)

newTree = Node(60)
newTree.insert(24)
newTree.insert(77)
newTree.insert(2)
newTree.printInOrder()
print(newTree.find(2))
newTree.printPreorder()
newTree.printPostorder()

