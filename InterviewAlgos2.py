import math 
from collections import Counter


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
	sq = sq - math.floor(sq)
	#If square root is equal to zero, it is a perfect square.
	if sq == 0:
		print("Yes!")
	else:
		print("No")

x = 52
isPerfectSquare(x)

#------------------------------------------------------------------------#

#Given an array of size n, find the majority element. The majority element is one that appears 
#more than n/2 times.

def findMajorityElement(arr):
	#Convert the list into a dictionary using the Counter() method.
	#having the elements as the keys and their frequencies as the values
	new_dict = Counter(arr)
	size = len(arr)

	for key, value in new_dict.items():
		#Now traverse the dictionary.The element whos frequency is greater than size / 2 is the majority element.
		if value > size / 2:
			print (key)
			return
	print ("None")

nums = [1,4,5,6,6,7,7,7,7,7]
findMajorityElement(nums)



#------------------------------------------------------------------------------------#

#Find the pivot element of an integer array.
#A pivot is defined as the index where the sum of the numbers on the left of the array are equal to the sum of the right.
#If there is no pivot return -1.

def findPivot(arr):
	right_sum = sum(arr)
	left_sum = 0
	for index, count in enumerate(arr):
		right_sum -= count
		if left_sum == right_sum:
			return index
		left_sum += count
	return -1

nums = [4,5,2,4,6,3,2]
nums2 = [4,6,77,5,89,2,1]
print (findPivot(nums))
print (findPivot(nums2))

#----------------------------------------------------------------------------#

#Given three points, check whether they lie on a straight collinear or not.
#i.e [[1,1], [1,4], [1,5]] is collinear
# [[1,5], [2,5], [4,6]] is not.
#Three points lie on a straight if the area if formed by the triangle of the three points is zero.
#Formula for Area of a triangle is  0.5 * [x1 * (y2 - y1) + x2 * (y3 - y2) + x3 * (y1 - y2)]

def isCollinear(x1, y1, x2, y2, x3, y3):
	#Calculate the area of a triangle.
	area = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
	if area == 0:
		return True
	else:
		return False


x1, x2, x3 ,y1, y2, y3 = 1,1,1,1,4,5
print (isCollinear(x1, y1, x2, y2, x3, y3))






