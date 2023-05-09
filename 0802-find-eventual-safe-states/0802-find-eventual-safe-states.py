class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        indegree = defaultdict(int)
        queue = deque()
        adjList = defaultdict(list)

        for index, neighbors in enumerate(graph):
            indegree[index] = len(neighbors)
            for neighbor in neighbors:
                adjList[neighbor].append(index)
            
        for node in range(len(graph)):
            if indegree[node] == 0:
                queue.append(node)

        while queue:
            currNode = queue.popleft()
            
            for neighbor in adjList[currNode]:
                indegree[neighbor] -= 1
                
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        safeNodes = []
        for node in range(len(graph)):
            if indegree[node] == 0:
                safeNodes.append(node)
        
        return safeNodes

