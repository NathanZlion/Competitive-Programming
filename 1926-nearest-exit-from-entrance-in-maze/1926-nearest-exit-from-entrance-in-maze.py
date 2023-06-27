class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        def isAnExit(row, col):
            return row == 0 or row == len(maze) - 1 or \
                   col == 0 or col == len(maze[0]) - 1

        def isInbound(row, col):
            return 0 <= row < len(maze) and 0 <= col < len(maze[0])

        directions = [ (0, 1), (0, -1), (1, 0), (-1, 0) ]
        queue = deque()
        maze[entrance[0]][entrance[1]] = '+'   # entrance does not count as exit

        for row, col in directions:
            row += entrance[0]
            col += entrance[1]

            if isInbound(row, col) and maze[row][col] == '.':
                queue.append((row, col))
        
        numberOfSteps = 0

        while len(queue) > 0:
            numberOfSteps += 1

            for _ in range(len(queue)):
                currRow, currCol = queue.popleft()
                
                if isAnExit(currRow, currCol):
                    return numberOfSteps
                
                for row, col in directions:
                    row += currRow
                    col += currCol

                    if isInbound(row, col) and maze[row][col] == ".":
                        queue.append((row, col))
                        maze[row][col] = "+"

        return -1
