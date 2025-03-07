def searchInSorted(arr, k):
    result = False
    n = len(arr)
    midIndex = n // 2 
    lastIndex = n - 1
    firstIndex = 0
    if(k==arr[midIndex]):
        result = True
    
    while(firstIndex <= lastIndex):
        midIndex = (firstIndex + lastIndex) // 2
        if(k == arr[midIndex]):
            result = True
        if(arr[midIndex]<k):
            firstIndex = midIndex + 1 
        else:
            lastIndex = midIndex - 1
    return result

L=[1,2,3,4,5,6,7,8,9]

# print(searchInSorted(L, 11))
# L= [1,2,3,4,5,6,7,8,9]
# L= [5,6,7,8,9]
# L= [7,8,9]
# L= [8,9]
# L= [9]


def findFirstOccurance(arr, k):
    n = len(arr)
    lastIndex = n - 1
    firstIndex = 0
    print(arr)
    while(firstIndex <= lastIndex):
        midIndex = (firstIndex + lastIndex) // 2
        print(firstIndex, midIndex, lastIndex)
        if(k > arr[midIndex]):
            firstIndex = midIndex + 1 
        elif(k < arr[midIndex]):
            lastIndex = midIndex - 1
        else:
            if(midIndex == 0 or arr[midIndex-1] != arr[midIndex]):
                return midIndex 
            else:
                lastIndex = midIndex - 1 
    return -1

def findLastOccurance(arr, k):
    n = len(arr)
    lastIndex = n - 1
    firstIndex = 0
    while(firstIndex <= lastIndex):
        midIndex = (firstIndex + lastIndex) // 2
        print(firstIndex, midIndex, lastIndex)
        if(k > arr[midIndex]):
            firstIndex = midIndex + 1 
        elif(k < arr[midIndex]):
            lastIndex = midIndex - 1
        else:
            if(midIndex == n-1 or arr[midIndex+1] != arr[midIndex]):
                return midIndex 
            else:
                firstIndex = midIndex + 1 
    return -1
L1=[2,2]
# print(findLastOccurance(L1, 2))

def countOnes(arr, N):
    return findLastOccurance(arr, N) + 1

def findLastOccurance(arr, N):
    n = len(arr)
    lastIndex = n - 1
    firstIndex = 0
    while(firstIndex <= lastIndex):
        midIndex = (firstIndex + lastIndex) // 2
        if(arr[midIndex] != 1):
            lastIndex = midIndex - 1
        else:
            if(midIndex == n-1 or arr[midIndex+1] != arr[midIndex]):
                return midIndex 
            else:
                firstIndex = midIndex + 1 
    return 0
L1=[1,0,0,0]
# print(countOnes(L1, len(L1)))

def f(n):
    if(n<=1):
        return 1
    if(n%2==0):
        return f(n//2)
    return f(n//2) + f(n//2+1)

# print(f(11)) 

def findLeftMostIndex(arr, X):
    n = len(arr)
    lastIndex = n - 1
    firstIndex = 0
    while(firstIndex <= lastIndex):
        midIndex = (firstIndex + lastIndex) // 2

        if(X > arr[midIndex]):
            firstIndex = midIndex + 1 
        elif(X < arr[midIndex]):
            lastIndex = midIndex - 1
        else:
            if(midIndex == 0 or arr[midIndex-1] != arr[midIndex]):
                return midIndex
            else:
               
                lastIndex = midIndex
    return -1

def findFloor(arr, k):
    n = len(arr)
    lastIndex = n - 1
    firstIndex = 0
    if(k < arr[0]):
        return -1
    if(k > arr[n-1]):
        return n-1
    while(firstIndex <= lastIndex):
        midIndex = (firstIndex + lastIndex) // 2
        print(firstIndex, midIndex, lastIndex)
        if(midIndex < 0 or  k < arr[midIndex] and k > arr[midIndex-1] ):
            return midIndex - 1 
        elif(midIndex >= n-1 or k > arr[midIndex] and k < arr[midIndex+1]):
            return midIndex
        elif(k > arr[midIndex]):
            firstIndex = midIndex + 1 
        elif(k < arr[midIndex]):
            lastIndex = midIndex - 1
        else:
            return midIndex
    return -1

L2 = [1, 2]
# print(findFloor(L2, 2))

def peakElement(arr):
    n = len(arr)
    if n == 1:
        return 0
    if n == 2:
        return 0 if arr[0] > arr[1] else 1

    firstIndex, lastIndex = 0, n - 1

    while firstIndex <= lastIndex:
        midIndex = (firstIndex + lastIndex) // 2

        if (midIndex == 0 or arr[midIndex] >= arr[midIndex - 1]) and \
           (midIndex == n - 1 or arr[midIndex] >= arr[midIndex + 1]):
            return midIndex

        if midIndex > 0 and arr[midIndex - 1] > arr[midIndex]:
            lastIndex = midIndex - 1
        else:
            firstIndex = midIndex + 1

    return -1 




def findElementRotatedArray2(arr, target):
    return getElement(arr, 0 , len(arr)-1, target)



    

def getElement(arr, start, end, target):
    if start > end:
        return -1

    if start == end - 1:
        if arr[start] == target:
            return start
        if arr[end] == target:
            return end
        return -1

    mid = (start + end) // 2 

    if arr[start] == target:
        return start
    if arr[mid] == target:
        return mid
    if arr[end] == target:
        return end

    if arr[start] < arr[mid]:  
        if arr[start] <= target < arr[mid]:  
            return getElement(arr, start, mid - 1, target)
        else:
            return getElement(arr, mid + 1, end, target)

    elif arr[mid] < arr[end]:  
        if arr[mid] < target <= arr[end]:  
            return getElement(arr, mid + 1, end, target)
        else:
            return getElement(arr, start, mid - 1, target)

    return -1 


L2 = [9,1,2,3,4]
print(findElementRotatedArray2(L2,5))  




