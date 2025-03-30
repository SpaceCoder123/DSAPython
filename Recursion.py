def getTotal(number):
    if(number <= 0):
        return 0
    if(number == 1):
        return 1
    return number%10 + getTotal(number//10)



def palindrome(string, start, end):
    if(start>=end):
        return True
    return string[start] == string[end] and palindrome(string, start+1, end-1)

palindromeString = "malayalam"
# print(palindrome(palindromeString,0, len(palindromeString)-1))

# You are given a number n. You need to recursively find the nth term of the series S that is given by:
# S(n) = n+ n*(S(n-1)) and S(0) = 1

def theSequence(n):
    if(n == 0):
        return 1
    theSequence(n-1)
    

# print(theSequence(2))

def printElements(arr,n):
    if(n==0):
        return 0 
    printElements(arr,n-1)
    print(arr[n-1] , end=" ")
    return 0


# printElements(L,len(L))

def CountDigits(n):
    if(n<1):
        return 0
    return CountDigits(n//10) + n%10

def recursiveSum(n):
    if(n<=1):
        return 1
    return recursiveSum(n-1) * n

# print(recursiveSum(4))

def fibonacci(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

# print(fibonacci(20))
# 0 1 1 2 3 5 8 13 21 34 55

def nCr(n,r):
    if(r==1):
        return n
    if(n==r):
        return 1
    return nCr(n-1,r-1) + nCr(n-1,r)

# print(nCr(5,2))

def isPalin(N):
    result = checkPalindrome(N, 0, len(N)-1)
    return 1 if(result == True) else 0 

def checkPalindrome(N, startIndex, endIndex):
    if(startIndex >= endIndex):
        return True
    return N[startIndex] == N[endIndex] and checkPalindrome(N, startIndex+1, endIndex-1)

# print(isPalin("malayalam"))


def ropeCuttingProblem(n, a, b, c):
    if n == 0:
        return 0
    
    if n <= 1:
        return -1
    
    res = max(ropeCuttingProblem(n-a, a,b,c), ropeCuttingProblem(n-b, a,b,c), ropeCuttingProblem(n-c, a,b,c))
    
    if(res == -1):
        return -1
    
    return res + 1

# print(ropeCuttingProblem(10,9,7,11))

# def checkString(string, first, last):
#     if first >= last:
#         return True
#     if string[first] != string[last]:
#         return False
#     return checkString(string, first+1, last-1)

# def recursivePalindromeCheck(string):
#     return checkString(string, 0, len(string)-1)

# print(recursivePalindromeCheck("ab"))

def power_set(s):
    result = []
    powerSet = 2**len(s)
    for i in range(powerSet):
        str = ""
        binary = bin(i)[2:].zfill(len(s))
        for j in range(len(binary)):
            if binary[j] == "1":
                str += s[j]
        result.append(str)
    return result

def sumOfDigits(number):
    if  number == 0:
        return 0
    else:
        return (number % 10) + sumOfDigits(number//10)

def countZero(number):
    if number == 0:
        return 0
    if number % 10 == 0:
        return 1 + countZero(number // 10)
    else:
        return countZero(number // 10)

def countOccurances(list, target):
    if(len(list) == 0):
        return 0
    
    if(list[0] == target):
        return 1+ countOccurances(list[1:], target)
    else:
        return countOccurances(list[1:], target)


# print(countOccurances([1,1,2,3,2,2,4],1))
# print(1//10)

# def myPow(base, exponent):
#     value = helper(base, abs(exponent))
#     return 1 / value if exponent < 0 else value

# def helper(base, exponent):
#     if exponent == 0:
#         return 1
#     if exponent == 1:
#         return base
    
#     half = helper(base, exponent // 2)
#     return half * half if exponent % 2 == 0 else half * half * base

# print(myPow(2,100))

# def getSubsets(arr):
    
# 53. Maximum Subarray
def maxSubArraySum(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    
    maxSum = arr[0]
    localSum = arr[0]
    
    for i in range(1,n):
        n = len(arr)
        if n == 0:
            return 0
        if n == 1:
            return arr[0]
        
        
        maxSum = arr[0]
        localSum = arr[0]
        
        for i in range(1,n):
            localSum = max(arr[i], arr[i] + localSum)
            maxSum = max(localSum, maxSum)
        return maxSum

# def firstMissingPositive(nums):
#     smallest = float("inf")
#     for i in nums:
#         if i < smallest and i >= 0:
#             i = smallest

# print(maxSubArraySum([-8, -3, -6, -2, -5, -4]))


def RecursionSubset(nums, rest):
    if len(rest) == 0:
        return [nums]
    
    curr = rest[:1]
    left = RecursionSubset(nums+curr, rest[1:])
    right = RecursionSubset(nums, rest[1:])

    left.extend(right)     
    return left

# print(RecursionSubset([],[1,2,2]))

# def RecursionSubsetNonRepeating(nums, rest):
#     if len(rest) == 0:
#         return [nums]
    
#     curr = rest[:1]
#     left = RecursionSubsetNonRepeating(nums+curr, rest[1:])
#     right = RecursionSubsetNonRepeating(nums, rest[1:])

#     unique_subsets = set(tuple(subset) for subset in (left + right))

#     return [list(subset) for subset in unique_subsets]

def bracketGenerator(string, counter, limit):

    if(counter == limit):
        return [string]
    
    left = bracketGenerator("()"+string, counter+1, limit)
    middle = bracketGenerator("("+string+")", counter+1, limit)
    right = bracketGenerator(string+"()", counter+1, limit)

    left.extend(middle)
    left.extend(right)

    return list(set(left))

# print(bracketGenerator("",0,4)) 
# ["((())())","(())()()","(()(()))","((()))()","()(()())","(()()())","()(())()","()()()()","((()()))","()()(())","(()())()","()((()))","(((())))"]
# ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]


# (())(())


def reverseNumber(number, reversed = 0):
    if number <= 0:
        return reversed
    remainder = number % 10
    reversed = (reversed * 10) + remainder
    return reverseNumber(number // 10, reversed)

def pow(base, exponent):
    if exponent == 0:
        return 1
    if exponent % 2 == 0:
        return pow(base * base, exponent//2) 
    else:
        return base * pow(base, exponent-1)
# print(reverse_exponentiation(3))

def reverse_exponentiation(n):
    return pow(n,reverseNumber(n))

def reverseNumber(number, reversed = 0):
    if number == 0:
        return reversed
        
    remainder = number % 10
    reversed = ( reversed * 10 ) + remainder
    return reverseNumber(number // 10, reversed)


def pow(base, exponent):
    if exponent == 0:
        return 1
    if exponent > 0:
        if exponent % 2 == 0:
            return pow(base * base, exponent//2)
        else:
            return base * pow(base, exponent - 1)
    else:
        if exponent % 2 == 0:
            return pow(1/(base * base), -exponent//2)
        else:
            return 1/(base * pow(base, -exponent - 1))


# bro the edge cases are annoying man
# print(pow(2,-2))

def bracketGenerator(number):
    brackets = []
    
    def bracketHelper(string, left, right):
        if len(string) == 2 * number:
            brackets.append(string)
            return
        
        if left < number:
            bracketHelper(string + "(", left + 1, right)
        
        if right < left:
            bracketHelper(string + ")", left, right + 1)

    bracketHelper("", 0, 0)
    return brackets

# print(bracketGenerator(3))

def permute(string):
    string.sort()
    permutationsResult = []

    def permutations(index):
        n = len(string)
        if index == n:
            permutationsResult.append(string[:])
            return 
        for i in range(index, n):
            string[i] , string[index] = string[index] , string[i]
            permutations(index+1)
            string[i] , string[index] = string[index] , string[i]

    permutations(0)
    return permutationsResult


print(permute([1,1,5]))


def nextPermutation(string):

    permutationsResult = []
    def permutations(index):
        n = len(string)
        if index == n and flag:
            if flag:
                permutationsResult.extend(string)
            else:
                flag = True
            return 
        
        for i in range(index, n):
            string[i] , string[index] = string[index] , string[i]
            permutations(index+1)
            string[i] , string[index] = string[index] , string[i]

    permutations(0)
    return permutationsResult
# print(permute([3,2,1]))