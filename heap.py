'''
#use Python's heapq module to make heaps.
import heapq

li = [2,56,"Ziggy", 9,"Tatooine"]

#Uses heapify to convert a list to a heap.
def makeHeap(list_to_heapify):
	heapq.heapify(list_to_heapify)
	print list_to_heapify

#Using heappush to push elements into a heap.
def pushToHeap(list_to_push, num):
	heapq.heappush(list_to_push, num)
	print list_to_push

#Pops the smallest element from a heap.
def popFromHeap(array):
	heapq.heappop(array)
	print array

makeHeap(li)
pushToHeap(li, 66)
popFromHeap(li)
'''

#Create a heap class setting heap to an array and current size for tracking size.
class binaryHeap:
	def __init__(self, array):
		self.heapList = array
		self.currentSize = 0

	"""
	First we want to find the parent index of the last element we inserted.
	Then, if that index value is less than the parent index we need to swap them to keep our heap property intact. 
	Now, we set a temp var to the heap list of parentindex value- to hold the value, 
	set the heaplist of parent index to the list index and the list index to the temp var.
	Finally, we set the actual
	"""

	#TODO FIX BUBBLE UP 
	def bubbleUp(self, index):
		parentIndex = (index - 1) //2
		if self.heapList[index] < self.heapList[parentIndex]:
			self.heapList[index], self.heapList[parentIndex] = self.heapList[parentIndex], self.heapList[index]
			index = parentIndex
			print self.heapList
			self.bubbleUp(index)			

	def bubbleDown(self, index):
		#Initally set as the root node of the tree.
		parentIndex = index
		leftChild = 2 * index + 1
		rightChild = 2 * index + 2
		if self.heapList[parentIndex] > self.heapList[leftChild]:
			self.heapList[parentIndex], self.heapList[leftChild] = self.heapList[leftChild], self.heapList[parentIndex]
			#parentIndex is increased because the leftChild it swapped with is at the next index.
			index = parentIndex + 1
			print self.heapList
			self.bubbleDown(index)
		else:
		    if self.heapList[parentIndex] > self.heapList[rightChild]:
				self.heapList[parentIndex], self.heapList[rightChild] = self.heapList[rightChild], self.heapList[parentIndex]
				index = parentIndex + 2
				print self.heapList
				self.bubbleDown(index)
			


	"""
	Replace the root node with the last element in the heap, (most bottom and furtherest to right side)
	Then delete the last element in the heap.
	Decrease the size of the heap, then in order to retain the heap property because the root node may not fit the min/max heap property,
	We must bubble it down to retain the heap.
	"""
	def delete(self):
		lastNode = self.heapList[-1]
		self.heapList[0] = lastNode
		self.currentSize -= 1
		self.heapList.pop()
		self.bubbleDown(0)


	"""
	Insert method that appends a node to our heaplist and adds to the size counter.
	Insert only adds the element, which causes a problem. We need to bubble it up to retain the min heap property. 
	We can do this by recursively calling the our Bubble up function.
	"""
	def insert(self, node):
		self.heapList.append(node)
		self.currentSize += 1
		#Marks it's index as the last index in the heap.
		index = self.currentSize
		self.bubbleUp(index)


arr = [10,12,18,23]
newHeap = binaryHeap(arr)
newHeap.delete()




