
from collections import defaultdict, deque


n, m = map(int, input().split())
adjList = defaultdict(list)
edges : list[tuple]= []


for _ in range(m):
    node1, node2= map(int, input().split())
    adjList[node1].append(node2)
    adjList[node2].append(node1)
    edges.append((node1, node2))

"""
-1 => uncolored
1 => source
0 => sink
"""
color = [-1 for _ in range(n+1)]

start_node = 1
queue = deque()
queue.append(start_node)
color[start_node] = 1

while queue:
    curr = queue.popleft()

    for neighbor in adjList[curr]:
        if color[neighbor] == color[curr]:
            print("NO")
            exit()

        if color[neighbor] == -1:
            queue.append(neighbor)
            color[neighbor] = 1 - color[curr]


print("YES")
res = []
for node1, _ in edges:
    res.append("0" if color[node1] == 1 else "1")

print("".join(res))
