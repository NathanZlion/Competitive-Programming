class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        maxArea = 0
        rowLength = len(grid)
        colLength = len(grid[0])


        def isInBoundAndLand(row, col):
            return (0 <= row < rowLength) \
                    and (0 <= col < colLength) \
                    and grid[row][col] == 1


        def dfs(row, col):
            grid[row][col] = 0
            count = 1
            
            for x,y in directions:
                if isInBoundAndLand(row+x, col+y):
                    count += dfs(row+x, col+y)
            
            return count


        for row in range(rowLength):
            for col in range(colLength):
                if grid[row][col] == 1:
                    maxArea = max(dfs(row, col), maxArea)


        return maxArea
