class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        gridSize = len(grid)

        queue = deque()

        def isInbound(row, col):
            return 0 <= row < gridSize and 0 <= col < gridSize

        if grid[0][0] == 0:
            queue.append((0,0))

        grid[0][0] = 1
        pathLength = 1

        while len(queue) > 0:
            n = len(queue)
            for _ in range(n):
                row, col = queue.popleft()

                if row == gridSize-1 and col == gridSize-1:
                    return pathLength

                for r, c in directions:
                    if isInbound(row+r, col+c) and grid[row+r][col+c] == 0:
                        grid[row+r][col+c] = 1
                        queue.append((row+r, col+c))

            pathLength += 1


        return -1
        