class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # start with all zeros
        res = [[0] * k for _ in range(k)]
        """
        Make row and col graph from given edges, then traverse to get a
        topologically sorted order. return the res at any time there is a cycle.
        """
        # make row graph
        rowIndegree = defaultdict(int)
        rowAdjList = defaultdict(list)

        for _above, _below in rowConditions:
            rowIndegree[_below] += 1
            rowAdjList[_above].append(_below)
        
        # topological sort traversal
        queue = deque()
        for node in range(1, k+1):
            if rowIndegree[node] == 0:
                queue.append(node)
        
        rowOrder = []
        while queue:
            curr = queue.popleft()
            rowOrder.append(curr)
            
            for neighbor in rowAdjList[curr]:
                rowIndegree[neighbor] -= 1
                if rowIndegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(rowOrder) != k:
            return []

        # make col graph
        colIndegree = defaultdict(int)
        colAdjList = defaultdict(list)

        for _left, _right in colConditions:
            colIndegree[_right] += 1
            colAdjList[_left].append(_right)
        
        # topological sort traversal
        for node in range(1, k+1):
            if colIndegree[node] == 0:
                queue.append(node)
        
        colOrder = []
        while queue:
            curr = queue.popleft()
            colOrder.append(curr)
            
            for neighbor in colAdjList[curr]:
                colIndegree[neighbor] -= 1
                if colIndegree[neighbor] == 0:
                    queue.append(neighbor)
        
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
