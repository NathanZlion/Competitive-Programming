class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        row_len = len(grid)
        col_len = len(grid[0])

        def is_inbound(row, col):
            return 0 <= row < row_len and 0 <= col < col_len
        
        def explore(row: int, col: int, grid: List[List[str]]) -> None:
            stack = [(row, col)]

            while stack:
                row, col = stack.pop()
                grid[row][col] = "0"
                for r, c in directions:
                    r += row
                    c += col
                    if is_inbound(r, c) and grid[r][c] == "1":
                        stack.append((r, c))            

        _count = 0
        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == "1":
                    explore(row, col, grid)
                    _count += 1

        return _count