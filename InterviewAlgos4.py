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
    
