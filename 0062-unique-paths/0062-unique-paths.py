class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]*n for _ in range(m)]
        grid[0][0] = 1
        
        def is_inbound(row: int, col: int) -> bool:
            return 0 <= col < n and 0 <= row < m
        
        for row in range(m):
            for col in range(n):
                if is_inbound(row-1, col):
                    grid[row][col] +=  grid[row-1][col]
                
                if is_inbound(row, col-1):
                    grid[row][col] +=  grid[row][col-1]

        return grid[m-1][n-1]