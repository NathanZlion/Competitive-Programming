class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def isInbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                top = grid[row-1][col] if isInbound(row-1, col) else None
                left = grid[row][col-1] if isInbound(row, col-1) else None

                if top != None and left != None:
                    grid[row][col] = grid[row][col] + min(top, left)

                elif top != None:
                    grid[row][col] = grid[row][col] + top

                elif left != None:
                    grid[row][col] = grid[row][col] + left


        return grid[-1][-1]