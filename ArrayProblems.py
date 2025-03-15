# Left Rotate by d Places
def rotateArray(arr, d): 
    n = len(arr)
    if n <= 1:
        return arr
    
    d = d % n 
    return arr[d:] + arr[:d]

# O(n) time complexity
# O(n) space complexity

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotateArray(arr, d):
    n = len(arr)
    if n <= 1:
        return
    d = d % n
    reverse(arr, 0, n-d - 1)
    reverse(arr, n-d, n - 1)
    reverse(arr, 0, n - 1)
    return arr


# O(n) time complexity
# O(1) space complexity


# 442. Find All Duplicates in an Array
def findDuplicates(nums):
    items = []
    value = 0
    for i in range(len(nums)):
        value = abs(nums[i])
        if(nums[value-1] < 0):
            items.append(value)
        nums[value - 1] = -nums[value - 1]
    return items

# 448. Find All Numbers Disappeared in an Array
def findDisappearedNumbers(nums):
    items = []
    value = 0
    for i in range(len(nums)):
        value = abs(nums[i])
        if(nums[value-1] < 0):
            continue
        nums[value - 1] = -nums[value - 1]

    for i in range(len(nums)):
        if(nums[i] > 0):
            items.append(i+1)
    return items

# 268. Missing Number

def missingNumber(nums):
    n = len(nums)
    total = n * (n + 1) // 2
    arraySum = sum(nums)
    return total - arraySum
        
# O(n) time complexity
# O(1) in worst space
print(missingNumber([1,1]))