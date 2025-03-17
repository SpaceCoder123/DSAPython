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

def maximumSubarraySum(arr, k):
    n = len(arr)
    if k > n:
        return []
    
    total = 0
    for i in range(k):
        total+= arr[i]

    curr = total
    left = 0
    right = k

    while right < n:
        curr = curr - arr[left]
        curr += arr[right] 
        right+=1
        left+=1
        if(curr>total):
            total = curr
    return total

def longestEvenSubArray(arr):
    return arr

def majorityElement(arr):
    n = len(arr)
    if n == 0: 
        return 0
    if n == 1:
        return arr[0]
    
    curr = arr[0]
    count = 0
    for i in range(1,n):
        if arr[i] == curr:
            count+=1
        if arr[i] != curr:
            if count == 0:
                curr = arr[i]
            else:
                count-=1

    majorityCount = 0
    for i in range(n):
        if(arr[i] == curr):
            majorityCount+=1
    
    
    return curr if majorityCount > n // 2 else -1

def maxProfit(prices):
    if not prices or len(prices) < 2:
        return 0
    
    min_price = prices[0]
    max_profit = 0 
    
    for price in prices[1:]:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit

def maxProfitMed(prices):
    n = len(prices)
    if n <= 1:
        return 0
    maxProfit = 0
    for i in range(1, n):
        profit = prices[i] - prices[i-1]
        if profit > 0:
            maxProfit+=profit
    return maxProfit


print(maxProfitMed([2, 1, 4, 5, 2, 9, 7]))