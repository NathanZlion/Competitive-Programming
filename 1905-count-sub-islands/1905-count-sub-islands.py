class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # find islands in grid 2
        # check if it's a sub island.
        
        island = []
        rowLength = len(grid2)
        colLength = len(grid2[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        count = 0

        def isInboundAndLand(row, col):
            return 0 <= row < rowLength and 0 <= col < colLength and grid2[row][col] == 1

        def isSubIsland(island: List[int]) -> bool:
            for row, col in island:
                if grid1[row][col] == 0:
                    return False
            
            return True


        def dfs(row, col) -> None:
            nonlocal island

            island.append((row, col))
            grid2[row][col] = 0

            for r, c in directions:
                if isInboundAndLand(row + r, col + c):
                    dfs(row + r, col + c)

        
        for row in range(rowLength):
            for col in range(colLength):
                if isInboundAndLand(row, col):
                    island.clear()
                    dfs(row, col)
                    count += 1 if isSubIsland(island) else 0

        return count
