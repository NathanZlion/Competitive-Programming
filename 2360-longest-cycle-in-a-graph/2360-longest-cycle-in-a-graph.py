class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        indegree = defaultdict(int)

        # traverse the edges to calculate indegree
        for from_, to_ in enumerate(edges):
            if to_ != -1:
                indegree[to_] += 1
            
        queue = deque()
        for node in range(len(edges)):
            if indegree[node] == 0:
                queue.append(node)
        
        while queue:
            curr = queue.popleft()
            indegree[curr] = 0
            
            if edges[curr] == -1:
                continue

            if indegree[edges[curr]] == 1:
                queue.append(edges[curr])
            
            indegree[edges[curr]] -= 1

        # now we're left with nodes that are in cycles
        def findCycleLength(node):
            curr = node
            length = 0

            while indegree[curr]:
                indegree[curr] -= 1
                curr = edges[curr]
                length += 1
            
            return length
        
        longestCycle = 0

        for node in range(len(edges)):
            if indegree[node] > 0:
                longestCycle = max(longestCycle, findCycleLength(node))

        return longestCycle if longestCycle else -1
