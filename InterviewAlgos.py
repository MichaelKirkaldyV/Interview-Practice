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

#print "The max depth of this tree is...", maxDepth(root)
#print "The min depth of this tree is...", minDepth(root)

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







