from collections import deque

#Pronouned "deck" meaning double-ended queue that supports adding and removing from either side of the in O(1) time.
#Deque's support removing and adding from either side, they can serve both as queues and stacks. 
#Stacks are "LIFO", Last in first out.
#Queues are "FIFO", First in first out.

newDeque = deque()

newDeque.append("apple")
newDeque.append("mango")
newDeque.append("grapes")
newDeque.append("mulberries")
newDeque.popleft()
newDeque.pop()

#For stricter implementations in Python
#If you're using a list there's nothing stopping a programmer from calling "insert", "remove" 
#or other list functions that will throw off your stack.
#We can create classes to ensure these valid operations can be performed.

class Stack:
	def __init__(self):
		self.stack = []

	def push(self, item):
		self.stack.append(item)

	def pop(self):
		if len(self.stack) < 1:
			return None
		else:
			return self.stack.pop()

	def size(self):
		return len(self.stack)

class Queue:
	def __init__(self):
		self.queue = []

	def enqueue(self, item):
		self.queue.append(item)

	def dequeue(self):
		if len(self.queue) < 1:
			return None
		else:
			return self.queue.pop(0)

	def size(self):
		return len(self.queue)


nStack = Stack()
nStack.push("Pomelo")
nStack.push("Currants")
print nStack
