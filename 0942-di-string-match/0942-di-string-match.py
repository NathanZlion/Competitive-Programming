class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        adjList = defaultdict(list)
        indegree = defaultdict(int)
        for i in range(n):
            if s[i] == 'I':
                adjList[i].append(i+1)
                indegree[i+1] += 1
            else:
                adjList[i+1].append(i)
                indegree[i] += 1

        queue = deque()
        for i in range(n+1):
            if indegree[i] == 0:
                queue.append(i)

        res = [0 for _ in range(n+1)]
        count = 0
        while queue:
            curr = queue.popleft()
            res[curr] = count
            count += 1
            
            for neighbor in adjList[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return res