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
