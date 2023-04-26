class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 0 => empty cell
        # 1 => fresh oranges
        # 2 => rotten oranges
        
        """
        using a queue start exploring.
        
        Till the queue is empty increment the number of minutes.
        When the queue is empty:
            return the number of minutes.
        """
        
        M = len(grid)
        N = len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def isInbound(row, col):
            return 0 <= row < M and 0 <= col < N

        def allRotten() -> bool:
            for row in range(M):
                for col in range(N):
                    if grid[row][col] == 1:
                        return False
            
            return True
                
            
        # first add all rotten tomatoes into the queue
        queue = deque()
        for row in range(M):
            for col in range(N):
                if grid[row][col] == 2: # if rotten
                    queue.append(((row, col)))

        minutesPassed = 0

        while len(queue) > 0:

            for _ in range(len(queue)):
                currRow, currCol = queue.popleft()

                # rot neighbors 4 directionally
                for r,c in directions:
                    if isInbound(currRow + r, currCol + c):
                        if grid[currRow + r][currCol + c] == 1:       # if it's fresh
                            grid[currRow + r][currCol + c] = 2        # rot the fresh tomato
                            queue.append((currRow + r, currCol + c))  # add it to the queue
                
            if len(queue) > 0: minutesPassed += 1

        return minutesPassed if allRotten() else -1

        