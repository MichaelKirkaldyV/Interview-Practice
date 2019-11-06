from collections import deque
"""
#Given a Binary Tree, find the maximum depth.
#Given a Binary Tree, find the minimum depth.


class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


def maxDepth(node):
	if node is None:
		return 0
	else:
		#Check the depth of left subtree and the right, recursively.
		left_depth = maxDepth(node.left)
		right_depth = maxDepth(node.right)

		#Add 1 to count the root node in the depth, as trees start at the 0 index.
		if left_depth > right_depth:
			return left_depth + 1
		else:
			return right_depth + 1

def minDepth(node):
	if node is None:
		return 0
	
	#Base Case. Only recognizing the root node.
	if node.left is None and node.right is None:
		return 1
	
	#If the left subtree is None, recursively check the right.
	if node.left is None:
		return minDepth(node.right) + 1

	#If the right subtree is None, recursively check the left.
	if node.right is None:
		return minDepth(node.left) + 1

	return min(minDepth(node.left), minDepth(node.right)) + 1



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print "The max depth of this tree is...", maxDepth(root)
print "The min depth of this tree is...", minDepth(root)

#-----------------------------------------------------------------------------------------#

#Given two Binary strings, return their sum. (Also, a Binary String)

def makeBinaryString(str1, str2):
	#First convert to integer
	#Then use bin to get the binary representation of that number.
	#splice from starting at two and then stop to remove "0b" get a clean value of the binary representation
	return bin(int(str1, 2) + int(str2, 2)) [2:]
	
a = "11"
b = "1"

makeBinaryString(a,b)
print makeBinaryString(a,b)
"""

#-----------------------------------------------------------------------------------#

#Given an array nums and a value val, remove all instances of that value in place and return the new length.
#Slicing a list goes as follows. list[<start>:<stop>:<step>]
def removeElement(arr, val):
	for i in range(len(arr)) [::-1]:
		if arr[i] == val:
			del arr[i]		
	return len(arr)

#Alternate method
def removeElement2(arr, val):
	for i in range(len(arr)):
		if arr[i] == val:
			arr.remove(arr[i])

nums = [1,2,2,3,4,5,2,7]
removeElement(nums, 2)
print removeElement(nums, 2)

#----------------------------------------------------------------------------------------#

#Given an expression string, write a program to check if a string has valid parenthesis.


def checkString(input_str):
	dic = {"(" : ")", "{" : "}", "[" : "]" }
	stack = deque()
	for parenthesis in input_str:
		#If the item is in the dictionary add it to the stack.
		if parenthesis in dic:
			stack.append(parenthesis)
		#check if the stack is empty(Base case) or if dic key isn't equal to parenthesis.
		elif len(stack) == 0 or dic[stack.pop()] != parenthesis:
			return False
	return True



new_string = "(){}[]"
str2 = "())))"
print checkString(new_string)
print checkString(str2)


#----------------------------------------------------------------------------------#

#Return the first occurence of the needle in the haystack.
#i.e haystack = "hello", needle = "ll"

def findNeedle(haystack, needle):
	if needle in haystack:
		#Use find() to find the first occurence of the needle.
		return haystack.find(needle)
	else:
		return 0

haystack = "Super Mario"
needle = "Mario"
h2 = "Nebula"
n2 = "Kowloon"
print findNeedle(h2, n2)
print findNeedle(haystack, needle)


#-------------------------------------------------------------------------------------#

#Given an array, rotate the array to the right by k steps, where k is non negative.
#i.e arr = [1,2,3,4,5,6,7] --> arr = [5,6,7,1,2,3,4]

def rotateArray(arr, step):
	if step == 0:
		return arr
	else:
		#take the no of steps to the end of the arr by slicing and the take the arr until the no of steps.
		#then add them and return the entire arr.
		return arr[:] = arr[-step:] + arr[:-step]


arr = [0,1,2,3,4,5,6,7]
print rotateArray(arr, step)










