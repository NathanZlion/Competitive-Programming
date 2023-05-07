

from collections import defaultdict


n = int(input())
adjList = defaultdict(list)

for _ in range(n):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

# find a starting node
start = -1

for node in adjList:
    if len(adjList[node]) == 1:
        start = node
        break

stack = [start]
visited = set()
route = []

while stack:
    currNode = stack.pop()
    route.append(currNode)
    visited.add(currNode)

    for neighbor in adjList[currNode]:
        if not neighbor in visited:
            stack.append(neighbor)

print(*route)




