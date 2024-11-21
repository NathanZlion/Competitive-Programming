class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        NOT_GUARDED = 0
        GUARDED = 1
        WALL = 2
        GUARD = 3
        BLOCKERS = set([WALL, GUARD])
        
        grid = [[ NOT_GUARDED for _ in range(n)]  for _ in range(m)]
        
        for row, col in walls:
            grid[row][col] = WALL
        
        for row, col in guards:
            grid[row][col] = GUARD
        
        def is_inbound(row, col):
            return 0 <= row < m and 0 <= col < n
        
        directions = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        for row, col in guards:
            for dr, dc in directions:
                r, c = row + dr, col + dc
                while is_inbound(r, c) and grid[r][c] not in BLOCKERS:
                    grid[r][c] = GUARDED
                    r += dr
                    c += dc
        
        count = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == NOT_GUARDED:
                    count += 1
        
        return count
        