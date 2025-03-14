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
