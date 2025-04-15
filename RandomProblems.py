import sys

def reverse(x):
    INT_MAX, INT_MIN = 2**31 - 1, -2**31
    final = 0
    neg = x < 0
    x = abs(x)
    
    while x != 0:
        remainder = x % 10
        x //= 10
        final = final * 10 + remainder  
        
        # Check for overflow
        if final > INT_MAX:
            return 0

    return -final if neg else final

thisdict = {
  1 : "I",
  5:  "V",
  10: "X",
  50:  "L",
  100 : "C",
  500: "D",
  1000: "M",    
}

def returnRomanNumber( placeValue, number):
    firstSymbol = ""
    midSymbol = ""
    lastSymbol = ""
    if(placeValue == 0):
        firstSymbol = thisdict[1]
        midSymbol = thisdict[5]
        lastSymbol = thisdict[10]
    elif(placeValue == 1):
        firstSymbol = thisdict[10]
        midSymbol = thisdict[50]
        lastSymbol = thisdict[100]
    elif(placeValue == 2):
        firstSymbol = thisdict[100]
        midSymbol = thisdict[500]
        lastSymbol = thisdict[1000]
    else:
        return number*"M"
    if(number==0):
        return ""
    elif(number == 4):
        return firstSymbol+midSymbol
    elif(number == 5):
        return midSymbol
    elif(number == 9):
        return firstSymbol+lastSymbol
    elif(number >= 1 and number < 4):
        return number*firstSymbol
    elif(number >= 6 and number < 9):
        return midSymbol+ (number % 5)* firstSymbol
    else:
        return firstSymbol
        
def intToRoman(num):
    finalNumeral = ""
    placeValue = 0
    while(num > 0):
        finalNumeral = returnRomanNumber(placeValue, num%10) + finalNumeral
        num = num // 10
        placeValue+=1
       
    return finalNumeral

# print(intToRoman(10))

def maxFrequencyElements(arr):
    return 

def sumExists(arr, N, sum):
    leftPtr = 0
    while(leftPtr < N):
        curr = arr[leftPtr]
        difference = abs(curr - sum)
        # print(difference, curr)
        if(curr > sum):
            leftPtr+=1
            continue
        elif(difference == curr):
            leftPtr+=1
            continue
        elif(difference in arr):
            return 1
        leftPtr+=1
    return 0
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sumExists(L, len(L), 14))

def linearProbing(hashSize, arr, sizeOfArray):
    finalArray = hashSize * [-1]
    for i in range(sizeOfArray):
        index = arr[i] % hashSize
        if(finalArray[index ] == -1):
            finalArray[index] = arr[i]
        else:
            finalIndex = (index + 1) % hashSize
            while(finalIndex != index):
                if(finalArray[index] == -1):
                    finalArray[index] =  arr[i]
                else:
                    index +=1
                
            # for i in arr:
    return finalArray  
L = [9,99,999,9999]
# print(linearProbing(10, L, len(L)))   

def firstRepeated(arr):
    mydict = {}
    n = len(arr)
    iter = n - 1
    minIndex = iter
    while(iter>=0):
        if(arr[iter] in mydict.keys()):
            if(iter < minIndex):
                minIndex = iter
        mydict[arr[iter]] = iter
        iter -= 1
    return -1 if(minIndex==n-1) else minIndex + 1
# print(firstRepeated([1, 1 ,5 , 7 ,6, 1, 4, 2 ,3 ,2, 2, 1,6, 8, 5, 7,6, 1, 8 ,9 ,2 ,7, 9, 5, 4 ,3 ,1])),
 

# sampleInput = {john,johnny,jackie,johnny,john,jackie,jamie,jamie,john,johnny,jamie,johnny,john} 
def winner(arr, n):
    mydict = {}
    for i in arr:
        if(i in mydict.keys()):
            mydict[i] +=1
        else:
            mydict[i] = 1

    highestElectedMember = arr[0]
    highestVotes = 0

    for i in mydict:
        if(mydict[i] > highestVotes ):
            highestElectedMember = i
            highestVotes = mydict[i]
        elif(mydict[i] == highestVotes):
            if(i<highestElectedMember):
                highestElectedMember = i
    return highestElectedMember 
L=["xqdou","igxji", "flkpn"]
# print(winner(L, len(L)))

def nonRepeatingChar(string):
    mydict = {}
    for i in string:
        if(i in mydict.keys()):
            mydict[i] +=1
        else:
            mydict[i] = 1

    character = ""
    for i in mydict:
        if(mydict[i] == 1):
            character = i
            break
    return character if(character!="") else -1 
# print(nonRepeatingChar("aabbccc"))

def printNonRepeated(arr):
    mydict = {}
    for i in arr:
        if(i in mydict.keys()):
            mydict[i] +=1
        else:
            mydict[i] = 1
    arr.clear()
    for i in mydict:
        if(mydict[i] == 1 ):
            arr.append(i)
    return arr 

L = [10, 20, 30, 40, 10]
# print(printNonRepeated(L))


def separateChaining( hashSize, arr, sizeOfArray):
    hashTable = [[] for i in range(hashSize)]   
    for i in range(sizeOfArray):
        index = arr[i] % hashSize
        hashTable[index].append(arr[i])
    return hashTable
L = [92,4,14,24,44,91]
# print(separateChaining(10,L, len(L)))


def maxFrequencyElements(arr):
    mydict = {}
    for i in arr:
        if(i in mydict.keys()):
            mydict[i] +=1
        else:
            mydict[i] = 1

    maxFrequencyElement = -1
    carry = 1
    for i in mydict:
        if(mydict[i] > maxFrequencyElement ):
            maxFrequencyElement = mydict[i]
            carry=1
        elif(mydict[i] == maxFrequencyElement):
            carry+=1 
    return maxFrequencyElement*carry 
# L = [1,2,3,4,5]
# print(maxFrequencyElements(L))

from OOPS.BinaryTree import BinaryTree

def preorder(root):
    return


def two_sum(nums, target):
    nums_with_index = [(num, i) for i, num in enumerate(nums)]
    nums_with_index.sort() 
    # print(nums_with_index)

    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums_with_index[left][0] + nums_with_index[right][0]
        if current_sum == target:
            return [nums_with_index[left][1], nums_with_index[right][1]]
        elif current_sum < target:
            left += 1 
        else:
            right -= 1

    return []
    

L = [3,2,4]



# 3. Longest Substring Without Repeating Characters
# def lengthOfLongestSubstring(s):
#     mydict = {}
#     rightPtr = 0
#     leftPtr = 0
#     n = len(s)
#     curr = 0
#     while(rightPtr < n):
#         if(s[rightPtr] not in mydict):
#             mydict[s[rightPtr]] = rightPtr
#             curr+=1
#         else:



#     return totalCount
# print(lengthOfLongestSubstring("dvdf"))

# mydict = {"a":1, "b":1}
# print("a" in mydict)
a= [1,2,3,4,5]
# print(-6/132)

# def sortColors(nums):
#     collection = {}
#     for i in nums:
#         if i in collection:
#             collection[i] += 1
#         else:
#             collection[i] = 1
#     return [0] * collection[0] + [1] * collection[1] + [2] * collection[2]


def sortColors(nums):
    collection = {}
    for i in nums:
        if i in collection:
            collection[i] += 1
        else:
            collection[i] = 1
    return [0] * collection[0] + [1] * collection[1] + [2] * collection[2]

# print(sortColors([2,0,2,1,1,0]))

# 1752. Check if Array Is Sorted and Rotated
def checkIfSortedAndRotated(nums):
    n = len(nums)
    if(n <= 1):
        return True
    
    last = n-1
    first = 1
    prev = 0
    count = 0


    if(nums[prev] < nums[last]):
        count+=1

    while(first < n):
        if(nums[prev] > nums[first]):
            count+=1
        # print(nums[prev], nums[last])
        first+=1
        prev +=1
    return count <= 1

# print(checkIfSortedAndRotated([5,1,5,1]))

# just take the minimum and maximum simoultaneously and find the difference
def maxAbsDiff(arr, n):

	minEle = arr[0]
	maxEle = arr[0]
	for i in range(1, n):
		minEle = min(minEle, arr[i])
		maxEle = max(maxEle, arr[i])

	return (maxEle - minEle)

# Driver code
# arr = [0, 1, 5, 3]
# n = len(arr)
# print(maxAbsDiff(arr, n))

# Two Sum II - Input Array Is Sorted // is this really medium level question LOL

def twoSumSorted(numbers, target):
    leftPointer = 0
    rightPointner = len(numbers)-1
    while(leftPointer < rightPointner):
        total = numbers[leftPointer] + numbers[rightPointner]
        if total > target:
            rightPointner-=1
        elif total == target:
            return [leftPointer+1, rightPointner+1]
        else:
            leftPointer+=1

# print(twoSumSorted([-1,0],-1))

import OOPS.Queue.QueueStructure as Queue

def checkQueue():
    q = Queue.MyQueue()
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.printQueue()

checkQueue()