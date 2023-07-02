

from collections import defaultdict, deque


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    degree = defaultdict(int)
    adjList = defaultdict(list)

    for _ in range(m):
        u, v = map(int, input().split())
        adjList[u].append(v)
        adjList[v].append(u)
        degree[u] += 1
        degree[v] += 1

    queue = deque()
    x = 0
    y = 0

    # collect one degree nodes
    for node, deg in degree.items():
        if deg == 1:
            queue.append(node)

    x = len(queue)

    for _ in range(len(queue)):
        node = queue.popleft()
        degree[node] = 0

        for neighbor in adjList[node]:
            degree[neighbor] -= 1
            if degree[neighbor] == 1:
                queue.append(neighbor)

    y = len(queue)
    x //= y

    print(y, x)



    

        

