from random import shuffle
from itertools import permutations


#Fibnacci sequence
#0,1,1,2,3,5,8,13,21,34,55,89,144
#F(n) = F(n-1) + F(n-2)

"""
def fibonacci(n):
	#First number in fib sequence is 0
	if n <= 0:
		print(0)
	#The second and third numbers are also 1
	elif n == 1:
		print(1)
	else:
		#Return the sum of the previous two term for next term in sequence
	 	return fibonacci(n-1) + fibonacci(n-2)

for n in range (1, 101):
	print(n, ":", fibonacci(n))
"""
#--------------------------------------------------------#

"""
FizzBuzz
If a number is a multiple of 3 return fizz
If it is a multiple of 5 return buzz
If it is a multple of both return fizzbuzz
"""


def fizzbuzz():
	for n in range(1, 101):
		if n % 3 == 0:
			print ("Fizz")
		elif n % 5 == 0:
			print ("buzz")
		elif n % 5 == 0 and n % 3 == 0:
			print ("FizzBuzz")

fizzbuzz()


#-----------------------------------------------------------------------------#


"""
Write a function that returns true if a string is a palindrone and false if it is not.
A Palindrom is a word that is the same reverse as it is initially.
"""

def isPalindrone(str1):
	rev_str = str1[::-1]
	if str1 == rev_str:
		return True
	else:
		return False

print(isPalindrone("gag"))
print(isPalindrone("Kamehameha"))


#A function that returns multiple Palindomes.

def getPalindromes(input_str):
	#Seperate the sentence into substrings.
	words = input_str.split()
	for word in words:
		if word == word[::-1]:
			print("Palindrome found! - ", word)
		else:
			None
	

sentence = "The concert starts at noon"
getPalindromes(sentence)

#----------------------------------------------------------------------#

#randomize items in a list.

def shuffleList(list1):
	return shuffle(list1)


x = ["matey", 1, 5, "Brink"]
print(shuffleList(x))

#-----------------------------------------------------------------------#

#Multiply strings and return a string value.

def multiplyStrings(str1, str2):
	return str(int(str1) * int(str2))

a = "56"
b = "34"
print(multiplyStrings(a,b))

#--------------------------------------------------------------------------#

#Find permutations in a set on n elements.

def findPermutations(list_):
	#Using pythons itertools and permutations
	plist = list(permutations(range(1,4)))
	return plist

list_ = [2,3,9]
print(findPermutations(list_))

#---------------------------------------------------------------#

#Find the kth largest element in an array.

def findKthElement(arr, k):
	#sorts backwards from biggest to smallest.
	arr.sort(reverse = True)
	print(arr)
	#subtract 1 from k to get kth largest, since lists count from 0
	return arr[k-1]

list_ = [4,7,9,3,5,90]
k = 3
print(findKthElement(list_, k))

#----------------------------------------------------------------#

#Find the missing elements in an array.

def findMissingElements(arr):
	#Using a list comprehension to return a list of all the indexes not in the list.
	print([x for x in range(arr[0], arr[-1], +1) if x not in arr])

list_2 = [1,3,4,5,7,9,10]
print(findMissingElements(list_2))

#------------------------------------------------------------------#

#Find the repeating elements in an array.

def findRepeatingElements(arr):
	arr_size = len(arr)
	for i in range(0, arr_size):
		#Check the next index and compare them.
		for j in range(i + 1, arr_size):
			if arr[i] == arr[j]:
				print(arr[i], "is a repeating element")

list_3 = [1,2,3,4,4,5,2,5,6,7,9,9]
findMissingElements(list_3)

#---------------------------------------------------------------------#

#Find the largest, second largest and the smallest in an unsorted integer array.

def findLargeSmallSlarge(arr):
	#Sort the list to put things in order from small to large.
	arr.sort()
	largest = arr[-1]
	smallest = arr[0]
	sec_largest = arr[-2]
	return largest, smallest, sec_largest

list_4 = [6,7,8,999,234356,6,78,1]
print(findLargeSmallSlarge(list_4))

#---------------------------------------------------------------------#

#Check to see if a string contains only numbers/digits.

def checkString(str1):
	#returns a boolean value of true if the string is full of numbers.
	return str1.isdigit()

new_string1 = "85635"
new_string2 = "Let's have some fun."
print(checkString(new_string1))
print(checkString(new_string2))








