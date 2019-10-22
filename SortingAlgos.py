"""
Bubble Sort is a simple sorting algorithm that iterates over alist,
comparing elements in pairs and swapping them until the larger elements bubble up to the end of the list
and the smaller elements stay at the beginning.

If the 1st element is larger than the 2nd then we swap them. If they are already - we leave them as is.
This continues until the last element in the list. Upon reaching the last element, it repeats this process
for every item in the list (quite inefficient). 
To optimize, we need to stop the algorithm when we're done sorting. 
We can use the swapped value! If nothing was swapped then we can stop the algorithm.
"""
#Time Complexity O(n^2)
def bubbleSort(arr):
	#Swapped is initialized as true so that the algo can run at least the first time. 
	swapped = True
	while swapped:
		swapped = False
		for i in range(len(arr) - 1):
			if arr[i] > arr[i + 1]:
				arr[i], arr[i + 1] = arr[i + 1], arr[i]
				swapped = True
	print arr

#list_of_nums = [3,72,35,546,68]
#bubbleSort(list_of_nums)


"""
Selection Sort segments the list into two parts: sorted and unsorted. We continuosly move the smallest element
of the unsort segment and add it to the sorted list.

We don't need to create a new list! we treat the leftmost part of the list as sorted and the right unsorted. 
We search the entire list for the smallest element and swap it with the first item.
Once we know the 1st element is sorted, we grab the smallest element of the unsorted list and swap it with the 2nd element and so on..
As i increases we have less items to check.
"""
#Time Complexity: O(n^2)
def selectionSort(arr):
	for i in range(len(arr)):
		#Assumes first element is sorted!
		lowest_value = i
		for j in range(i + 1, len(arr)):
			if arr[j] < arr[lowest_value]:
				lowest_value = j
				arr[i], arr[lowest_value] = arr[lowest_value], arr[i]

#list_of_nums = [2,56,25,77,8990,88]
#selectionSort(list_of_nums)
#print list_of_nums

"""
Insertion Sort, like selection sort it segments the list into sorted and unsorted parts. 
It iterates over the unsorted list and inserts the element being viewed into the correct postion in the sorted list.

We start by assuming the first element(i) of the list is sorted. We then move to the next element(x), if element if x is smaller we do nothing
otherwise we set (x) to the 1st element (i) and set (i) to (x).
As we move to the other elements in the sorted list, we continuosly move larger elements in teh sorted segment up until we encounter a smaller element.
or reach the end of the sorted list, then we place (x) in it's place.
""" 

def insertionSort(arr):
	for index in range(1,len(alist)):
	    currentvalue = alist[index]
	    print currentvalue
	    position = index
	    while position > 0 and alist[position-1] > currentvalue:
	        alist[position] = alist[position-1]
	        position = position-1
	    alist[position] = currentvalue
alist = [90,56,2,566,1,12,22]
insertionSort(alist)
print alist










