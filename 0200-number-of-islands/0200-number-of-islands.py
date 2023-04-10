class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rowLength = len(grid)
        colLength = len(grid[0])
        neighbors = [(0,1),(1,0),(0,-1),(-1,0)]
        isInbound = lambda row, col: 0 <= row < rowLength and 0 <= col < colLength

        def bfs(row, col):
            nonlocal grid

            queue = deque()
            queue.append((row,col))

            while len(queue) > 0:
                r,c = queue.popleft()

                for neighbor in neighbors:
                    nRow, nCol = r + neighbor[0], c + neighbor[1]
                    if isInbound(nRow, nCol) and grid[nRow][nCol] == "1":   # a land neighbor not explored yet
                        grid[nRow][nCol] = "2"
                        queue.append((nRow, nCol))


        for row in range(rowLength):
            for col in range(colLength):
                if isInbound(row, col) and grid[row][col] == "1":
                    grid[row][col] = "2"
                    count += 1
                    bfs(row, col)


        return count
