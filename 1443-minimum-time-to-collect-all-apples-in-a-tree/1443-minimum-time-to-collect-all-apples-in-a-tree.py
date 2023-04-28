class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        """
        construct an undirected adjecency list from the given edges.
        using the adjecency list do a dfs and for every node check if it has children.
        """
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
                childHasApple = dfs(child)
                if childHasApple:
                    pathCost += 2
                    appleExistsInSubTree = True

            return hasApple[node] or appleExistsInSubTree

        dfs(0)
        return pathCost
