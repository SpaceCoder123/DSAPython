

# for node, neighbors in graph.items():
#     print("{} node is conencted to {}".format(node, neighbors))


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
    'A': ['B','C','E'],
    'B': ['C','A', 'D'],
    'C': ['A', 'B','D'],
    'D': ['C', 'B'],
    'E': ['A']
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

print(dfs(graph,"A"))            