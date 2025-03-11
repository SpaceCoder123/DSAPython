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

print(ropeCuttingProblem(23,5,13,5))