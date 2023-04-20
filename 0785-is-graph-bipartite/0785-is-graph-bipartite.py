class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # team1 = 1
        # team2 = -1
        # uncolored = 0

        N = len(graph)
        color = [0 for _ in range(len(graph))]

        def dfs(node:int, prevColor: int = 1):
            nonlocal color

            # if not explored already:
            if color[node] == 0:
                # explore it, set color opposite to current
                color[node] = -prevColor

                # dfs it's neighbors
                for neighbor in graph[node]:
                    if not dfs(neighbor, -prevColor):
                        return False

            # if this color is same as incoming color return False else True
            return color[node] != prevColor

        for i in range(N):
            if color[i] == 0:
                if not dfs(i):
                    return False

        return True