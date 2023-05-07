
from collections import deque


t = int(input())

def isInbound(row, col):
    return 0 <= row < 2 and 0 <= col < numOfCol

for _ in range(t):
    numOfCol = int(input())
    board = []
    board.append([int(num) for num in input()])   # row 1
    board.append([int(num) for num in input()])   # row 2

    # do a bfs
    goalState = (1,numOfCol-1)
    reached = False
    start = (0,0)
    directions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
    queue = deque()
    queue.append(start)

    while len(queue) > 0:
        currRow, currCol = queue.pop()
        if (currRow, currCol) == goalState:
            reached = True
            break

        for newRow, newCol in directions:
            newRow += currRow
            newCol += currCol

            if isInbound(newRow, newCol) and board[newRow][newCol] == 0:
                board[newRow][newCol] = 1
                queue.append((newRow, newCol))

    print("YES" if reached else "NO")


