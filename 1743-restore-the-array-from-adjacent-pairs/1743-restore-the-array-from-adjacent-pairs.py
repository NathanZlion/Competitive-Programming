class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:        

        adjList = defaultdict(list)
        degree = defaultdict(int)
        
        for node1, node2 in adjacentPairs:
            adjList[node1].append(node2)
            adjList[node2].append(node1)
            degree[node1] += 1
            degree[node2] += 1
        
        stack = []
        for node, deg in degree.items():
            if deg == 1:
                stack.append(node)
                break
        
        path = []
        while stack:
            curr = stack.pop()
            path.append(curr)
            degree[curr] = 0

            for neighbor in adjList[curr]:
                if degree[neighbor] == 0:
                    continue
                
                degree[neighbor] -= 1
                if degree[neighbor] <= 1:
                    stack.append(neighbor)

        return path
