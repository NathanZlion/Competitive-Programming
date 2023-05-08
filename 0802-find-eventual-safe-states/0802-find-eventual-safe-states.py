class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        # lets do bfs implementation of this
        
        adjList = defaultdict(list)
        
        indegree = defaultdict(int)
        
        for index, neighbors in enumerate(graph):
            indegree[index] = len(neighbors)
            for neighbor in neighbors:
                adjList[neighbor].append(index)
        
        queue = deque()
        safeNodes = []
        
        for index in range(len(graph)):
            if indegree[index] == 0:
                queue.append(index)
                safeNodes.append(index)

        while queue:
            currNode = queue.pop()
            
            for neighbor in adjList[currNode]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    safeNodes.append(neighbor)
                    queue.append(neighbor)


        return sorted(safeNodes)