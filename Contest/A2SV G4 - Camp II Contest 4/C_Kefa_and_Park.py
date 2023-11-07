from collections import defaultdict

numOfVertices, maxConsecCats = map(int, input().split())
hasCat = list(map(int, input().split()))

graph = defaultdict(list[int])

# take the edges input and build graph
for _ in range(numOfVertices - 1):
    ver1, ver2 = map(int, input().split())
    node1 = min(ver1, ver2) - 1
    node2 = max(ver1, ver2) - 1
    graph[node1].append(node2)

def numOfValidPaths(vertex: int, consecCats: int) -> int:    
    if hasCat[vertex] == 1:
        consecCats += 1
    else:
        consecCats = 0

    if consecCats > maxConsecCats:
        return 0

    # is a leaf node
    if len(graph[vertex]) == 0:
        return 1

    validPaths = 0
    for nextVertex in graph[vertex]:
        validPaths += numOfValidPaths(nextVertex, consecCats)

    return validPaths

print(numOfValidPaths(0, 0))