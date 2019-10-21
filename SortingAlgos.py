
def bubbleSort(arr):
	swapped = True
	while swapped:
		swapped = False
		for i in range(len(arr) - 1):
			if arr[i] > arr[i + 1]:
				arr[i], arr[i + 1] = arr[i + 1], arr[i]
				swapped = True
	print arr

list_of_nums = [3,72,35,546,68]
bubbleSort(list_of_nums)
print len(list_of_nums)

