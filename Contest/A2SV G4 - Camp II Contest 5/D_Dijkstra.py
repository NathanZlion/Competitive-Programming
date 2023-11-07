from collections import defaultdict
from heapq import heappop, heappush
 
n, m = map(int, input().split())
adjList = defaultdict(list)
minDist = {1: 0} 
parent = {1:-1}

for _ in range(m):
    a, b, w = map(int, input().split())
    adjList[a].append((b, w))
    adjList[b].append((a, w))

pq = [(0, 1)]
while pq:
    cost, node = heappop(pq)

    for child, weight in adjList[node]:
        if child in minDist and minDist[child] <= cost + weight:
            continue
 
        minDist[child] = cost + weight
        parent[child] = node
        heappush(pq, (minDist[child], child))
 
if n not in minDist:
    print(-1)
else:
    res = []
    curr = n
    while curr in parent:
        res.append(curr)
        curr = parent[curr]
 
    print(*res[::-1])
