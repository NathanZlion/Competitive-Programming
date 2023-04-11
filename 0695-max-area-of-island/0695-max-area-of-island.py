
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


        def getAreaOfIsland(row, col):
            
            area = 0
            stack = []
            stack.append((row, col))
            
            while stack:
                r,c = stack.pop()
                grid[r][c] = 0
                area += 1

                for neighbor in directions:
                    newRow, newCol = r + neighbor[0], c + neighbor[1]
                    if isInBoundAndLand(newRow, newCol):
                        grid[newRow][newCol] = 0
                        stack.append((newRow, newCol))

            return area


        for row in range(rowLength):
            for col in range(colLength):
                if grid[row][col] == 1:
                    maxArea = max(getAreaOfIsland(row, col), maxArea)


        return maxArea
