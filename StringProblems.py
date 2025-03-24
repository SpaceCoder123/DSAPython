# def count_distinct_vowels(s):
#     vowels = {'a', 'e', 'i', 'o', 'u'}  # Set of vowels
#     found_vowels = 0  # To count distinct vowels as a bitmask
#     mask = 0  # Bitmask to track found vowels

#     for char in s:
#         print(mask)
#         if char in vowels:
#             bit = 1 << (ord(char) - ord('a'))
#             print(mask, bit)
#             if not (mask & bit):  # Check if vowel is already counted
#                 mask |= bit  # Mark vowel as found
#                 found_vowels += 1
#                 if found_vowels == 5:  # All vowels found, stop early
#                     break

#     return found_vowels

# Example usage
# print(count_distinct_vowels("hello"))        # 2 (e, o)
# print(count_distinct_vowels("education"))    # 5 (a, e, i, o, u)
# print(count_distinct_vowels("rhythm"))       # 0
# print(count_distinct_vowels("banana"))       # 1 (a)
# print(count_distinct_vowels("eaiuo"))   # 5 (a, e, i, o, u)

def lengthString(self, str):
    #code here
    length = 0
    for _ in str:
        length+=1
    return length

def countVowels(self,s):
    #code here
    vowelsCount = 0
    found_vowels = ""
    vowels = {"a","e","i","o","u"}
    for i in s:
        if i in vowels and i not in found_vowels:
            vowelsCount+=1
            found_vowels += i
    
    return vowelsCount

def caseConversion(s):
    upperCase = ""
    for i in s:
        if ord(i) >= 97:
            upperCase+= chr(ord(i)-32)
        else:
            upperCase+=i
    return upperCase

def lowerCaseConversion(s):
    lowerCase = ""
    for i in s:
        if ord(i) < 97:
            lowerCase+= chr(ord(i)+32)
        else:
            lowerCase+=i
    return lowerCase



def reverseString(characters):
    # n = len(characters)
    # curr = 0
    # last = n - 1
    # for _ in range(n): 
    #     temp = characters[curr]
    #     characters[curr] = characters[last]
    #     characters[last] =  temp
    #     curr+=1
    #     last-=1
    # return characters
    return characters[::-1]

def areAnagrams(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    if(n1 != n2):
        return False
    
    s1Total = 0
    s2Total = 0
    for i in range(n1):
        s1Total+=ord(s1[i])
        s2Total+=ord(s2[i])


    output = s1Total == s2Total
    for i in range(0,n1):
        if s2[i] not in s1 and s1[i] not in s2:
            output = False
            break
    return output

def isPanagram(s):
    #97-122
    n = len(s)
    if(n <= 26):
        return False

    chars = ""
    for i in s:
        if ord(i) < 97:
            char = chr(ord(i)+32)
            if(char not in chars):
                chars += char
        else:   
            char = chr(ord(i))
            if(char not in chars):
                chars += char

    return len(chars) == 26

def missingPanagram(s): 
    missing = ""
    for i in range(97,123):
        if chr(i) in s or chr(i-32) in s:
            continue
        else:
            missing += chr(i)
        
    return -1 if len(missing) == 0 else missing    

# print(missingPanagram("Abcdefghijklmnopqrstuvwxy"))

def validate(s):
    hasHigherCase = False
    hasLowerCase = False
    hasSpecialCharacters = False
    hasNumbers = False
    hasLength = False

    if(len(s) <= 10):
        hasLength = True

    for i in s:
        value = ord(i)
        if value >= 48 and value <= 57:
           hasNumbers = True 

        if value >= 35 and value <= 38 or value == 64 or value == 45 or value == 42:
            hasSpecialCharacters = True  

        if value >= 97 and value <= 122:
            hasLowerCase = True 
        
        if value >= 65 and value <= 90:
            hasHigherCase = True 

    return 1 if(hasLowerCase and hasHigherCase and hasSpecialCharacters and hasNumbers and hasLength) else 0

print(validate("hella"))