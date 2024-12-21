class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # construct adjList
        adjList = defaultdict(list)
        
        for nodeA, nodeB in edges:
            adjList[nodeA].append(nodeB)
            adjList[nodeB].append(nodeA)

        visited = set()
        
        # do a dfs starting with the 0th node
        def dfs(node: int) -> Tuple[int, int]:
            visited.add(node)
            subtreeSum, subtreeCuts = values[node], 0
            
            for child in adjList[node]:
                if child not in visited:
                    childSum, childCut = dfs(child)
                    subtreeSum += childSum
                    subtreeCuts += childCut
            
            # curr subtree can be separated
            if subtreeSum % k == 0:
                subtreeCuts += 1
            
            return subtreeSum, subtreeCuts
        
        _, numOfCuts = dfs(0)
        return numOfCuts