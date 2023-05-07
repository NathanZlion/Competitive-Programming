

from collections import deque

totalRows, totalCols, maxNumOfActions = map(int, input().split())
board = []

for _ in range(totalRows):
    board.append([char for char in input()])

actions = list(map(int, input().split()))
actionToMove = {
    0: (0,0),   # staying
    1: (-1,0),   # up
    2: (1,0),   # down
    3: (0,-1),   # left
    4: (0,1),   # right
}

def isInbound(row, col):
    return 0 <= row < totalRows and 0 <= col < totalCols

mouseLocation = None

directions = [(1,0),(0,1),(-1,0),(0,-1)]

# walls len(actions+1)
for row in range(totalRows):
    for col in range(totalCols):
        if board[row][col] == "M":
            mouseLocation = (row, col)
            board[row][col] = 0
        
        elif board[row][col] == ".":
            board[row][col] = -1
        
        else:
            board[row][col] = 1_000_000_000

for index in range(len(actions)):
    action = actions[index]
    row, col = mouseLocation
    moveRow, moveCol = actionToMove[action]
    moveRow += row
    moveCol += col
    if isInbound(moveRow, moveCol) and board[moveRow][moveCol] != "#":
        row,col = moveRow, moveCol
    
    mouseLocation = (row,col)
    board[row][col] = max(board[row][col], index+1)

queue = deque()
for row in range(totalRows):
    for col in range(totalCols):
        if 0 <= board[row][col] <= maxNumOfActions:
            queue.append((row, col))

while len(queue) > 0:
    row, col = queue.popleft()

    for r, c in directions:
        r += row
        c += col

        if isInbound(r, c) and board[r][c] != "#" and board[r][c] < board[row][col]-1:
            board[r][c] = board[row][col]-1
            queue.append((r,c))


possibleStartingLocations = 0
for row in range(totalRows):
    for col in range(totalCols):
        if 0 <= board[row][col] <= maxNumOfActions:
            possibleStartingLocations += 1

print(possibleStartingLocations)
