from math import inf

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        rowLength = len(grid)
        colLength = len(grid[0])

        @cache
        def minFallSumForCell(row: int, col: int) -> int:
            # we've reached last row
            if row == rowLength - 1:
                return grid[row][col]
            
            minPathSum = inf
            for colBelow in range(colLength):
                if colBelow == col:
                    continue

                minPathSum = min(minPathSum, minFallSumForCell(row+1, colBelow))

            return minPathSum + grid[row][col]
        
        minPathSum = inf
        for col in range(colLength):
            minPathSum = min(minPathSum, minFallSumForCell(0, col))

        return minPathSum