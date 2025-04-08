def snakePattern(matrix):
    for i in range(len(matrix)):
        if i % 2 == 0:
            for j in range(len(matrix)):
                print(matrix[i][j], end=" ")
        else:
            for j in range(len(matrix)-1, -1, -1):
                print(matrix[i][j], end=" ")
    return matrix


# snakePattern(arr)

def findElementin2DMatrix(matrix, element):
    arr = []
    for i in range(len(matrix)):
        if element >= matrix[i][0] and element <= matrix[i][len(matrix[i])-1]:
            arr = matrix[i]

    if len(arr) == 0:
        return False
    return binarySearch(arr, 0, len(arr)-1, element)

def binarySearch(arr, first, last, element):
    if first > last:
        return False
        
    mid = (first+last)//2
    if arr[mid] == element or arr[first] == element or arr[last] == element:
        return True
    if arr[mid] < element:
        return binarySearch(arr, mid+1, last, element)
    else:
        return binarySearch(arr, first, mid-1, element)
 
# more optimization might be here
# current time complexity O(n * logn)
def findElementPart2(matrix, element):
    result = False
    for i in range(len(matrix)):
        if element >= matrix[i][0] and element <= matrix[i][len(matrix[i])-1]:
            result = binarySearch(matrix[i], 0, len(matrix[i])-1, element)
            if result:
                return True
    return result

def binarySearch(arr, first, last, element):
    if first > last:
        return False
        
    mid = (first+last)//2
    if arr[mid] == element or arr[first] == element or arr[last] == element:
        return True
    if arr[mid] < element:
        return binarySearch(arr, mid+1, last, element)
    else:
        return binarySearch(arr, first, mid-1, element)
    
def findWord(matrix, string):
    rows, cols = len(matrix), len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == string[0]:
                if findWordHelper(matrix, string, 0, i, j, set()):
                    return True
    return False

def findWordHelper(matrix, string, pointer, row, col, visited):
    if pointer == len(string):
        return True

    if not (0 <= row < len(matrix)) or not (0 <= col < len(matrix[0])):
        return False

    if matrix[row][col] != string[pointer] or (row, col) in visited:
        return False

    visited.add((row, col))

    found = (
        findWordHelper(matrix, string, pointer + 1, row + 1, col, visited) or
        findWordHelper(matrix, string, pointer + 1, row - 1, col, visited) or
        findWordHelper(matrix, string, pointer + 1, row, col + 1, visited) or
        findWordHelper(matrix, string, pointer + 1, row, col - 1, visited)
    )

    visited.remove((row, col))
    return found


def transposeOfAMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    return matrix

arr = [[1,2,3],[4,5,6],[7,8,9]]
# print(transposeOfAMatrix(arr))

def rotateMatrix(matrix):
    for i in range(len(matrix)):
        matrix[i].reverse()
    
    return matrix

print(rotateMatrix(transposeOfAMatrix(arr)))