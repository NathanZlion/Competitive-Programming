class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        adjList = defaultdict(list)
        degree = defaultdict(int)
        
        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)
            degree[node1] += 1
            degree[node2] += 1

        queue = deque()
        for node in range(n):
            if degree[node] == 1:
                queue.append(node)
        
        # hold a list of the maximum heights travelled from leaves to parents
        height = [0 for _ in range(n)]
        
        # update the child height with the maximum of parent height + 1 and it's current max height
        while queue:
            curr = queue.popleft()
            degree[curr] = 0

            for neighbor in adjList[curr]:
                # has not been popped
                if degree[neighbor] > 1:
                    height[neighbor] = max(height[curr] + 1, height[neighbor])
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        queue.append(neighbor)
        
        minimumHeight = max(height)

        return [index for index in range(n) if height[index] == minimumHeight]


