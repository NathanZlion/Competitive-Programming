from math import inf

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        rowLength = len(grid)
        colLength = len(grid[0])
        
        for row in range(rowLength-2, -1, -1):
            for col in range(colLength):

                minPathSumBelow = inf
                for colBelow in range(colLength):
                    if colBelow == col:
                        continue
                    
                    minPathSumBelow = min(minPathSumBelow, grid[row+1][colBelow])
                
                grid[row][col] += minPathSumBelow
        
        return min(grid[0])
                    