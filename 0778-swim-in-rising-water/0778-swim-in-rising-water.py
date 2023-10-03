class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows, cols = len(grid), len(grid[0])
        time = 0
        priorityQueue = [[grid[0][0], (0, 0)]]
        visited = set()
        
        def isInbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        while len(priorityQueue) > 0:
            elevation, (row, col) = heappop(priorityQueue)
            time = max(elevation, time)

            if row == rows-1 and col == cols-1:
                return time

            for r, c in directions:
                r += row
                c += col

                if isInbound(r, c) and (r,c) not in visited:
                    visited.add((r, c))
                    heappush(priorityQueue, [grid[r][c], (r, c)])

