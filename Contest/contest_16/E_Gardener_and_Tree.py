


# perform topological sorting and count vertices in cycle


from collections import defaultdict, deque


t = int(input())

for _ in range(t):
    input()

    n, k = map(int, input().split())
    adjList = defaultdict(list)
    degree = defaultdict(int)

    for _ in range(n-1):
        u, v = map(int, input().split())
        degree[u] += 1
        degree[v] += 1
        adjList[u].append(v)
        adjList[v].append(u)

    queue = deque()
    for node in degree:
        if degree[node] == 1:
            queue.append(node)

    iteration = 0
    visited = set()

    while queue:
        if iteration == k:
            break

        for _ in range(len(queue)):
            curr = queue.popleft()
            visited.add(curr)
            degree[curr] = 0

            for neighbor in adjList[curr]:
                if degree[neighbor] == 0:
                    continue

                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    queue.append(neighbor)

        iteration += 1

    count = 0
    for node in degree:
        if node not in visited:
            count += 1
    
    print(count)

