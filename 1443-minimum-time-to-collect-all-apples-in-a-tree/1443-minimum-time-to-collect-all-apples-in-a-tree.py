class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        adjList = defaultdict(list)
        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)

        pathCost = 0
        explored = set()
        explored.add(0)
        
        def dfs(node):
            nonlocal pathCost

            appleExistsInSubTree = False

            for child in adjList[node]:
                if child in explored:
                    continue

                explored.add(child)

                if dfs(child):
                    pathCost += 2
                    appleExistsInSubTree = True

            return hasApple[node] or appleExistsInSubTree

        dfs(0)
        return pathCost
