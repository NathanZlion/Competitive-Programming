class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        rowLength = len(maze)
        colLength = len(maze[0])
        
        def isInBound(row, col) -> bool:
            return 0 <= row < rowLength and 0 <= col < colLength
        
        def isAnExit(row, col) -> bool:
            return row == 0 or row == rowLength-1 or col == 0 or col == colLength-1

        queue = deque()
        maze[entrance[0]][entrance[1]] = '+'

        for newRow, newCol in directions:
            newRow += entrance[0]
            newCol += entrance[1]

            if isInBound(newRow, newCol) and maze[newRow][newCol] == '.':
                queue.append((newRow, newCol))
                maze[newRow][newCol] = '+'

        moves = 1
        while len(queue) > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if isAnExit(row, col):
                    return moves

                for newRow, newCol in directions:
                    newRow += row
                    newCol += col

                    if isInBound(newRow, newCol) and maze[newRow][newCol] == '.':
                        queue.append((newRow, newCol))
                        maze[newRow][newCol] = '+'

            moves += 1

        return -1
        