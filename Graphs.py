
from collections import deque

def addNode(source, destination):
    if source in graph:
        graph[source].append(destination)
    else:
        graph[source] = [destination]

    if destination in graph:
        graph[destination].append(source)
    else:
        graph[destination] = [source]
    return graph

def deleteNode(source):
    for i in graph.keys():
        if source in graph[i]:
            graph[i].remove(source)
    graph.pop(source, None)
    return graph

def deleteEdge(source, destination):
    if source in graph and destination in graph[source]:
        graph[source].remove(destination)
    if destination in graph and source in graph[destination]:
        graph[destination].remove(source)
    return graph

def getNeighbourNodes(source):
    if source in graph.keys():
        return graph[source]
    else:
        return "Node not available"

# print(getNeighbourNodes("E"))

def checkEdge(source, destination):
    if source in graph.keys():
        if destination in graph[source]:
            return True
    elif destination in graph.keys():
        if source in graph[destination]:
            return True
    return False

graph = {
    '0': ['1','3','4'],
    '1': ['C','0', '3'],
    'C': ['0', '1','3'],
    '3': ['C', '1'],
    '4': ['0']
}

def dfs(graph, start):
    def dfsHelper(start, hashArr):
        if len(hashArr) == len(graph):
            return hashArr
        
        neighbours = graph[start]

        for i in neighbours:
            if i not in hashArr:
                hashArr = dfsHelper(i, hashArr+[i])
            else:
                continue
        return hashArr     
    finalHash = dfsHelper(start, [start])
    return finalHash

def bfs(graph, start):
    visited = []
    myQueue = [start]
    while(len(myQueue) > 0):
        node = myQueue.pop(0)
        
        if node not in  visited:
            visited.append(node)
            
        neighbours = graph[node]
        for i in neighbours:
            if i in visited:
                continue
            myQueue.append(i)
    return visited
# print(bfs(graph,"A"))            

graphList = [[1, 2],[0, 3, 4],[0, 5],[1, 6],[1, 5],[2, 4, 7],[3, 7],[5, 6, 8],[7, 9],[8, 10, 11],[9],[9, 12],[11, 13],[12]]

def getShortestPath(graph, start, target):
    visited = [None] * len(graph) 
    visited[start] = 0
    queue = [start]
    parent = [None] * len(graph)

    while(len(queue) > 0):
        node = queue.pop(0)
        if node == target:
            break
        neighbours = graph[node]
        for i in neighbours:
            if visited[i] == None:
                visited[i] = visited[node] + 1
                parent[i] = node
                queue.append(i) 
    
    if visited[target] is None:
        return "path does not exist"

    path = []
    current = target
    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    return path
# print(getShortestPath(graphList, 0,6))


# lets do using adjacency matrix
matrix = [[0,1,1],[1,0,1],[1,1,0]]

# 0 1 1
# 1 0 1
# 1 1 0
def getAllNeighbours(matrix, node):
    neighbours = []
    row = matrix[node]
    for j in range(len(row)):
        if row[j] == 1:
            neighbours.append(j)
    return neighbours


def dfs(matrix):
    visited = [False] * len(matrix)
    nodes = []
    for k in range(len(visited)):
        if visited[k] == False:
            nodes.append(k)
            visited[k] = True
            neighnours = matrix[k]
            for i in range(len(neighnours)):
                if neighnours[i] == 1 and visited[i] == False: 
                    visited[i] = True
                    nodes.append(i)
    return nodes

def checkLoop(list, vertices):
    queue = [(0,0)]
    visited = [False] * vertices
    while(len(queue) > 0):
        queueItem = queue.pop(0)
        currNode = queueItem[1]
        parentNode = queueItem[0]
        neighbours = list[currNode]
        for neighbour in neighbours:
            
            visited[parentNode] = True
            if neighbour == parentNode:
                continue
            
            elif visited[neighbour] == True:
                return True

            else:
                queue.append((currNode, neighbour)) 
                   
    return False

cycleInput = [[1, 2], [0, 2], [0, 1]]

def checkGraphConnected(matrix):
    visited = [False] * len(matrix)

    def dfs(node):
        visited[node] = True
        for neighbor in range(len(matrix)):
            if matrix[node][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)

    dfs(0)

    return all(visited)

def minStepToReachTarget(knightPos, targetPos, n):
    visitedPoints = {}
    def helper(row, col, count):
        if row < 1 or col < 1 or row > n or col > n:
            return False
            
        if (row, col) in visitedPoints:
            if visitedPoints[(row,col)] >= count:
                return False
            else:
                visitedPoints[(row,col)] = count
        else:
            visitedPoints[(row,col)] = count
        
        if row == targetPos[0] and col == targetPos[1]:
            return True
            
        return (helper(row -2, col-1, count+1) 
                or helper(row -2, col+1, count+1)
                or helper(row -1, col-2, count+1) 
                or helper(row +1, col-2, count+1)
                or helper(row +2, col-1, count+1) 
                or helper(row +2, col+1, count+1) 
                or helper(row -1, col+2, count+1) 
                or helper(row -1, col+2, count+1))
    
    helper(knightPos[0], knightPos[1], 0)
    
    return visitedPoints[(targetPos[0], targetPos[1])]


def minStepToReachTarget(knightPos, targetPos, n):
    moves = [(-2, -1), (-2, +1), (-1, -2), (-1, +2),
             (+1, -2), (+1, +2), (+2, -1), (+2, +1)]

    visited = set()
    queue = [(knightPos[0], knightPos[1], 0)]
    visited.add((knightPos[0], knightPos[1]))

    while queue:
        row, col, steps = queue.pop(0)

        if (row, col) == (targetPos[0], targetPos[1]):
            return steps

        for move in moves:
            newRow = row + move[0]
            newCol = col + move[1]

            if 1 <= newRow <= n and 1 <= newCol <= n:
                if (newRow, newCol) not in visited:
                    visited.add((newRow, newCol)) 
                    queue.append((newRow, newCol, steps + 1))

    return -1



def numIslands(grid):
    # code here
    visited = set()
    n = len(grid)
    m = len(grid[0])
    totalIslands = 0
    def bfsIsland(row, col):
        queue = deque()
        queue.append((row,col))
        visited.add((row,col))
        moves = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        
        while(queue):
            r,c = queue.popleft()
            for move in moves:
                newRow = r + move[0]
                newCol = c + move[1]
                if newRow >=0 and newCol >=0 and newRow<n and newCol<m:
                    if(newRow, newCol) not in visited and grid[newRow][newCol] == "L":
                        queue.append((newRow,newCol))
                        visited.add((newRow,newCol))
                        
                
    for i in range(n):
        for j in range(m):
            if (i,j) not in visited and grid[i][j] == "L":
                bfsIsland(i,j)
                totalIslands+=1
                
    return totalIslands

def motherVortexBruteForce(vertices, adj):

    def bfs(node):
        visited = [False] * vertices
        queue = deque()
        queue.append(node)
        visited[node] = True
        while queue:
            current = queue.popleft()
            neighbours = adj[current]
            print(neighbours, visited)
            for neighbour in neighbours:
                if visited[neighbour] == False:
                    queue.append(neighbour)
                    visited[neighbour] = True
        return visited
    
    for i in range(vertices):
        result = bfs(i)
        if all(result):
            return i
    return -1

# still in progress


def orangesRotting(grid):
    n , m= len(grid), len(grid[0])
    visited = [[-1] * m for _ in range(n)]
    fresh = 0
    queue = deque() 
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                visited[i][j] == 0
                queue.append((i,j,0))
            elif grid[i][j] == 1:
                fresh+=1

    moves = [(1,0),(-1,0),(0,1),(0,-1)]
    max_time = 0
    rotted = 0

    while queue:
        r, c, t = queue.popleft()
        for dr, dc in moves:
            nr, nc = r+dr, c+dc
            if (0 <= nr < n and 0 <= nc < m
                and grid[nr][nc] == 1
                and visited[nr][nc] == -1):
                visited[nr][nc] = t+1
                queue.append((nr, nc, t+1))
                rotted += 1
                max_time = max(max_time, t+1)

    return max_time if rotted == fresh else -1

# print(orangesRotting( [[2,1,1],[1,1,0],[0,1,1]]))

# print(10**6-1)

def isEscapePossible(blocked, source, target):
    blocked_set = set(map(tuple, blocked))
    max_area = 20000

    def bfs(start, end):
        queue = deque([tuple(start)])
        visited = set([tuple(start)])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        steps = 0

        while queue and steps < max_area:
            r, c = queue.popleft()
            if [r, c] == end:
                return True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < 10**6 and 0 <= nc < 10**6:
                    if (nr, nc) not in visited and (nr, nc) not in blocked_set:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                        steps += 1
        return steps >= max_area

    return bfs(source, target) and bfs(target, source)

 
# print(isEscapePossible([[0,1],[1,0]],[0,0],[0,2]))

def levelOfX(V, adj, X):

    visited = set()
    queue = deque()
    queue.append((0,0))
    while queue:
        node, level = queue.popleft()
        visited.add(node)
        if node == X:
            return level
        
        neighbours = adj[node]
        for neighbour in neighbours:
            queue.append((neighbour, level+1))
    return -1


def isCycle(V, edges):
    adj = [[] for _ in range(V)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * V

    for i in range(V):
        if not visited[i]:
            queue = deque()
            queue.append((i, -1))
            visited[i] = True

            while queue:
                node, parent = queue.popleft()
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append((neighbor, node))
                    elif neighbor != parent:
                        return True 

    return False  # No cycle found

# edges = [[0, 4], [1, 2], [1, 4], [2, 3],[3, 4]]
# print(isCycle(5, edges))

def containsCycle(grid):
    n, m = len(grid), len(grid[0])
    visited = [[False] * m for _ in range(n)]
    def search(char, row, col, parentRow, parentCol):
        visited[row][col] = True
        moves = [(+1,0),(-1,0),(0,-1),(0,+1)]
        for dr, dc in moves:
            nr = dr + row
            nc = dc + col
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == char:
                if not visited[nr][nc]:
                    if search(char, nr, nc, row, col):
                        return True
                elif (nr, nc) != (parentRow, parentCol):
                    return True
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                if search(grid[i][j], i, j, -1, -1):
                    return True
    return False


grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
# print(containsCycle((grid)))

def xShape(grid):
    count = 0
    n, m = len(grid), len(grid[0])
    visited = [[False] * m for _ in range(n)]

    def getCount(row, col):
        moves = [(0,-1),(1,0),(-1,0),(0,1)]
        queue = deque([(row,col)])
        while(queue):
            node = queue.popleft()
            for move in moves:
                r,c = move
                newRow = node[0] + r
                newCol = node[1] + c
                if newRow < 0 or newCol < 0 or newRow >= n or newCol >= m:
                    continue
                if grid[newRow][newCol] == 'X' and not visited[newRow][newCol]:
                    visited[newRow][newCol] = True
                    queue.append((newRow, newCol))


    for row in range(n):
        for col in range(m):
            if grid[row][col] == "X" and visited[row][col] == False:
                count+=1
                getCount(row, col)

    return count

grid =  [["X","0","X"],["0","X","0"],["X","X","X"]]

def detectCycleDirectedGraph(V, edges):
    adj = [[] for _ in range(V)]
    pathVisited = [False] * V
    visited = [False] * V
    
    for u, v in edges:
        adj[u].append(v)

    def dfs(vertex):
        visited[vertex] = True
        pathVisited[vertex] = True
        neighbours = adj[vertex]
        for neighbour in neighbours:
            if not visited[neighbour]:
                if dfs(neighbour):
                    return True
            if pathVisited[neighbour] == True:
                return True
        pathVisited[vertex] = False
        return False

    for i in range(V):
        if visited[i] is False:
            if(dfs(i)):
                return True
    return False


def detectCycleDirectedGraph(V, edges):
    adj = [[] for _ in range(V)]
    pathVisited = [False] * V
    visited = [False] * V
    
    for u, v in edges:
        adj[u].append(v)

    def dfs(vertex):
        visited[vertex] = True
        pathVisited[vertex] = True
        neighbours = adj[vertex]
        for neighbour in neighbours:
            if not visited[neighbour]:
                if dfs(neighbour):
                    return True
            if pathVisited[neighbour] == True:
                return True
        pathVisited[vertex] = False
        return False

    for i in range(V):
        if visited[i] is False:
            if(dfs(i)):
                return True
    return False


grid = [[0, 1], [1, 2], [2, 3], [3, 1]]

def largestCycle(edges):
    totalLength = -1
    n = len(edges)
    adj = [[] for _ in range(n)]
    for i in range(n):
        if(edges[i] != -1):
            adj[i].append(edges[i])
        else:
            adj[i] = []

    
    weights = [0]*n
    visited = [False]*n


    def dfs(vertex, weight):
        if visited[vertex]:
            return weight - weights[vertex]
        else:
            weights[vertex] = weight
            visited[vertex] = True
            neighbours = adj[vertex]
            for neighbour in neighbours:
                value = dfs(neighbour, weight+1)
                return value
            return -1
    for i in range(n):
        if visited[i] == False:
            totalLength = max(totalLength, dfs(i, 0))

    return totalLength

# print(max(-1, 3))