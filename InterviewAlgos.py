#Given a Binary Tree, find the maximum depth.

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


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print "The max depth of this tree is...", maxDepth(root)




