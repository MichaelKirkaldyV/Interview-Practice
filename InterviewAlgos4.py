import itertools

# Write an Algorithm to count special character, digits, consonants or vowels in a string.
def countCharType(str_):
    #special char counts spaces as well.
    special_ch = 0
    digits = 0
    vowels = 0
    consonants = 0

    for index in range(0, len(str_)):
        char = str_[index]
        #Checks to see if the character of the string passed in is in the alphabet.
        if char >= "a" and char <= "z" or char >= "A" and char <= "Z":
            #changes all the values to lowercase for ease of use.
            char = char.lower()

            #Checks to see if the char value is a vowel.
            if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
                vowels += 1
            else:
                consonants += 1
        
        #Checks to see if the char value is a digit.
        elif char >= "0" and char <= "9":
            digits += 1
        else:
            special_ch += 1
    
    print("Special Character:", special_ch)
    print("Consonants:", consonants)
    print("Digits:", digits)
    print("Vowels:", vowels)

new_str = "Enemey Chopper ahead! Take Cover! 202"
countCharType(new_str)

#-------------------------------------------------------------#

# Given two integers, return all possible combinations of k and numbers out of 1....n
# Return type is a list.

def combinations(n, k):
    return list(itertools.combinations(range(1, n + 1), k))
n = 4
k = 2
print(combinations(n, k))

'''
Given an array, find the Peak element in the array. An array element is peak if it is not smaller than its neighbors(left, right)
i.e. arr - [5,10,20,15] 20 is the only peak element.
Corner cases give better idea about this problem.
If an input arry is sorted in increasing order the last element is always peak.
If an input array is sorted in decreasing order the first element is always peak.
Lastly, if all elements are the same then every element is peak.
'''

def findPeakUtility(arr, low, high, length):
    # Find the middle element.
    mid = low + high / 2
    mid = int(mid)

    # If element to the left of mid is less than mid and to right of mid is less, return the mid as peak value.
    # If mid is the 1st element return it as peak ( if sorted in decreasing order).
    # If mid is the last element return it as peak( if sorted in increasing order).
    if mid == 0 or arr[mid - 1] <= arr[mid]:
        if mid == n - 1 or arr[mid + 1] <= arr[mid]:
            return mid
    elif mid > 0 and arr[ mid - 1] > arr[mid]:
        return findPeakUtility(arr, low, mid - 1, n)
    else:
        return findPeakUtility(arr, low, mid + 1, n)


def findPeak(arr, length):
    # takes an array, lowest element, highest element and length of the array.
    return findPeakUtility(arr, 0, n - 1, n)

new_list = [1,3,20,4,1,0]
n = len(new_list)
print(findPeak(new_list, n))


'''
A simple Binary Search algo that after one check ignores half of the list.
Compares x with the middle element.
If x matches the middle element, we return it.
Else if x is greater than the middle element, then x can only be in the right half of the subarray.
If x is smaller, we recur for the left side.
'''

def binarySearch(arr, left, right, x):
    # Base Case
    if right > left:
        # Find the middle value
        mid = left + right / 2
        # List indices must be integers or slices, not floats.
        mid = int(mid)
        # Checks if the middle value is equal to x.
        if arr[mid] == x:
            return mid
        # If x is smaller than mid, it must be on the left side of the list.
        # If x is greater than mid, it'll be on the right side.
        elif x < arr[mid]:
            # Recur left side of the list
            return binarySearch(arr, 0, mid - 1, x)
        else:
            # Recur right side of the list
            return binarySearch(arr, 0, mid + 1, x)

list2 = [2,6,8,9990,35]
x = 35
print(binarySearch(list2, 0, len(list2) - 1, x))