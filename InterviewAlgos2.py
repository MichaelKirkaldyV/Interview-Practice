import math 


#Reverse a singly linked list
#[1,2,3,4,5] -> [5,4,3,2,1]

class Node:
	def __init__(self, value):
		self.value = value
		self.next_node = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.current_size = 0

	def insert(self, value):
		new_node = Node(value)
		if self.head == None:
			self.head = new_node
		else:
			current_node = self.head
			while current_node:
				if current_node.next_node == None:
					current_node.next_node = new_node
				else:
					current_node = current_node.next_node
			

	def reverse(self):
		previous_node = o
		current_node = self.head
		while (current_node is not None):
			next_node = current_node.next_node
			current_node.next_node = previous_node
			previous_node = current_node
			current_node = next_node
		self.head = previous_node

	def print(self):
		node = self.head
		while node:
			print (node.value)
			node = node.next_node

newList = LinkedList()
newList.insert(5)
newList.insert(7)
newList.insert(1)
newList.insert(20)
newList.print()
newList.reverse()
newList.print()

#------------------------------------------------------------------------------------------#

#Given a number, check to see if it is a perfect square or not.

def isPerfectSquare(integer):
	#take the square root.
	sq = math.sqrt(integer)
	#Take the floor/ceiling/round of the square root.
	#Subtract the value from the the floor/ceiling square root from the square root.
	sq = sq - math.floor(sqrt_)
	#If square root is equal to zero, it is a perfect square.
	if sq == 0:
		print("Yes!")
	else:
		print("No")

x = 52
isPerfectSquare(x)