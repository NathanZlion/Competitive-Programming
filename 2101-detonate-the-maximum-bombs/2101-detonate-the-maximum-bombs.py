class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        count = defaultdict(int)

        def eucledeanDistance(x1, y1, x2, y2):
            return ((y2-y1)**2 + (x2-x1)**2)**0.5

        adjList = defaultdict(list)

        # build your adj list
        numberOfBombs = len(bombs)

        for i in range(numberOfBombs):
            x1, y1, radius = bombs[i]
            count[(x1,y1)] += 1

            for j in range(numberOfBombs):
                if i == j:
                    continue
                x2, y2, rad2 = bombs[j]

                if eucledeanDistance(x1,y1,x2,y2) <= radius:
                    adjList[(x1,y1)].append((x2, y2))

        maxBlast = 0
        explored = set()

        def dfs(x, y):
            nonlocal explored
            count = 1

            if (x,y) in explored:
                return 0

            explored.add((x,y))
            
            for x2, y2 in adjList[(x,y)]:
                count += dfs(x2, y2)

            return count

        # do dfs for all nodes
        for bombx, bomby, raduis in bombs:
            maxBlast = max(dfs(bombx, bomby) + count[(bombx, bomby)] - 1, maxBlast)
            explored.clear()

        # return the maximum number of bombs detonated
        return maxBlast
        
        
        
        