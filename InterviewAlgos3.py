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

#--------------------------------------------------------#

FizzBuzz
If a number is a multiple of 3 return fizz
If it is a multiple of 5 return buzz
If it is a multple of both return fizzbuzz


def fizzbuzz():
	for n in range(1, 101):
		if n % 3 == 0:
			print ("Fizz")
		elif n % 5 == 0:
			print ("buzz")
		elif n % 5 == 0 and n % 3 == 0:
			print ("FizzBuzz")

fizzbuzz()
"""

#-----------------------------------------------------------------------------#

"""
Write a function that returns true if a string is a palindrone and false if it is not.
A Palindrom is a word that is the same reverse as it is initially.


def isPalindrone(str1):
	rev_str = str1[::-1]
	if str1 == rev_str:
		return True
	else:
		return False

print(isPalindrone("gag"))
print(isPalindrone("Kamehameha"))
"""

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



