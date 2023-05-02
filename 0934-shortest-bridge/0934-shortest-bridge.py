class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        n = len(grid)

        def isInbound(row, col):
            return -1 < row < n and -1 < col < n

        landRow, landCol = 0,0

        # finding a land from the first island
        for i in range(n*n):
            row = i//n
            col = i%n

            if grid[row][col] == 1:
                landRow, landCol = row, col
                break

        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        # discovering island one
        queue = deque()
        tempQueue = deque()
        tempQueue.append((landRow, landCol))
        grid[landRow][landCol] = 2

        while len(tempQueue) > 0:
            row, col = tempQueue.popleft()
            queue.append((row, col))

            for newRow, newCol in directions:
                newRow += row
                newCol += col

                if isInbound(newRow, newCol) and grid[newRow][newCol] == 1:
                    grid[newRow][newCol] = 2
                    tempQueue.append((newRow, newCol))


        # do a bfs from the discovered island one to find the second island
        moves = 0
        while len(queue) > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for newRow, newCol in directions:
                    newRow += row
                    newCol += col
                    
                    if not isInbound(newRow, newCol):
                        continue

                    if grid[newRow][newCol] == 1:
                        return moves

                    if grid[newRow][newCol] == 0:
                        queue.append((newRow, newCol))
                        grid[newRow][newCol] = 2

            moves += 1
