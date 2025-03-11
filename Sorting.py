def bubbleSort(arr):
    flag = 0
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1):
            if(arr[j] > arr[i]):
                arr[i],arr[j] = arr[j], arr[i]
                flag = 1
        if(flag == 0):
            return arr
    return arr

def selectionSort(arr):
    n = len(arr)
    for i in range(0, n-1):
        index = getSmallestElementIndex(arr, n, i)
        if(arr[i] > arr[index]):
            arr[i], arr[index] = arr[index], arr[i]
    return arr

def getSmallestElementIndex(arr,N, startIndex):
    index = startIndex
    for i in range(startIndex, N):
        if(arr[i] < arr[index]):
            index  = i
    return index

L = [64, 25, 12, 22, 11]
# print(selectionSort(L))

# [64, 25, 12, 22, 11]
L2 = [11, 25, 12, 22, 64]
# [11, 12, 25, 22, 64]
# [11, 12, 22, 25, 64]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements that are greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr

# print(insertion_sort(L))

L2 = [11,12,22,25,64]
L = [11,12,22,25,64]

def mergeTwoArrays(arr1, arr2):
    resultArray = []

    if(len(arr2) == 0 and len(arr1) == 0):
        return resultArray
    
    while(True):
        if(len(arr2) == 0):
            resultArray += arr1 
            break
        elif(len(arr1) == 0):
            resultArray += arr2 
            break
        elif(arr1[0] < arr2[0]):
            resultArray.append(arr1[0])
            arr1 = arr1[1:]
        else:
            resultArray.append(arr2[0])
            arr2 = arr2[1:] 
    return resultArray


def union_of_two_arrays(L1, L2):
    final_array = []
    i, j = 0, 0  # Two pointers

    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            if not final_array or final_array[-1] != L1[i]:
                final_array.append(L1[i])
            i += 1
        elif L1[i] > L2[j]:
            if not final_array or final_array[-1] != L2[j]:
                final_array.append(L2[j])
            j += 1
        else:  # L1[i] == L2[j], avoid duplicates
            if not final_array or final_array[-1] != L1[i]:
                final_array.append(L1[i])
            i += 1
            j += 1  # Skip duplicates in both lists

    # Add remaining elements from L1
    while i < len(L1):
        if final_array[-1] != L1[i]:
            final_array.append(L1[i])
        i += 1

    # Add remaining elements from L2
    while j < len(L2):
        if final_array[-1] != L2[j]:
            final_array.append(L2[j])
        j += 1

    return final_array

L1 = [2, 12, 22, 25, 64,73]
L3 = [11, 12, 25, 64]
# print(union_of_two_arrays(L1, L3))

# timeComplexity = O(n + m (while loop at the end))
# spaceComplexity = O(n)    

####################################

def intersectionOfTwoArrays(L1, L2):
    final_array = []
    i = 0

    while i < len(L1):
            if(L1[i] in final_array):
                i += 1
            else:
                if(L1[i] in L2):
                    final_array.append(L1[i])
                    i += 1
                else:
                    i += 1
    return final_array

# print(intersectionOfTwoArrays(L1, L3))

# timeComplexity = O(n)
# spaceComplexity = O(n) 

def binary_array_sorting(arr):
    left, right = 0, 0  # Two pointers

    while right < len(arr):
        if arr[right] == 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1  # Move `left` to track the next position for 0
        right += 1  # Always move `right` forward

    return arr

# Example usage:
arr = [1, 1, 0 ,0 ,1, 1 ,0 ,1 ,0 ,0]
# print(binary_array_sorting(arr))  # Output: [0, 0, 0, 0, 1, 1, 1, 1]

# timeComplexity = O(n) 
# spaceComplexity = O(1)


def merge2(nums1, m, nums2, n):
    i = m - 1 
    j = n - 1  
    k = m + n - 1
    
    
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    while j >= 0:
        nums1[k] = nums2[j]
        k -= 1
        j -= 1

    return nums1

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
            inversion+=1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return (merged)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid]) 
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)


print(merge_sort([2,1,4,3,7,8,5]))
# timeComplexity = O(n+m) 
# spaceComplexity = O(1)