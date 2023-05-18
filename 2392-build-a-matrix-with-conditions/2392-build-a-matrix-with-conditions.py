class Solution:
    
    def findTopologicalOrder(self, k, conditions):
        indegree = defaultdict(int)
        adjList = defaultdict(list)

        for _first, _second in conditions:
            indegree[_second] += 1
            adjList[_first].append(_second)

        # topological sort traversal
        queue = deque()
        for node in range(1, k+1):
            if indegree[node] == 0:
                queue.append(node)
        
        order = []
        while queue:
            curr = queue.popleft()
            order.append(curr)
            
            for neighbor in adjList[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return order
        
        
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # start with all zeros
        res = [[0] * k for _ in range(k)]

        rowOrder = self.findTopologicalOrder(k, rowConditions)

        if len(rowOrder) != k:
            return []

        colOrder = self.findTopologicalOrder(k, colConditions)
        
        if len(colOrder) != k:
            return []
        
        rowIndex = {}
        colIndex = {}
        
        for index, val in enumerate(rowOrder):
            rowIndex[val] = index

        for index, val in enumerate(colOrder):
            colIndex[val] = index
        
        for node in range(1, k+1):
            row, col = rowIndex[node], colIndex[node]
            res[row][col] = node

        return res
