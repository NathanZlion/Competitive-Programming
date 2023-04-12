class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # find islands in grid 2
        # check if it's a sub island.
        
        rowLength = len(grid2)
        colLength = len(grid2[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        count = 0

        def isInboundAndLand(row, col):
            return 0 <= row < rowLength and 0 <= col < colLength and grid2[row][col] == 1

        def dfs(row, col) -> bool:
            
            valid = grid1[row][col] == 1
            

            grid2[row][col] = 0

            for r, c in directions:
                if isInboundAndLand(row + r, col + c):
                    valid = dfs(row + r, col + c) and valid

            return valid


        for row in range(rowLength):
            for col in range(colLength):
                if isInboundAndLand(row, col):
                    count += 1 if dfs(row, col) else 0

        return count
