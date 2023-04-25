

arow, acol = 2,3
n = 8
board = [[True for _ in range(n)] for _ in range(n)]

def isAttackable(row, col):
    return row == arow or col == acol or abs(row-arow)==abs(col-acol)

def isInbound(row, col):
    return 0 <= row < n and 0 <= col < n

for r in range(n):
    for c in range(n):
        board[r][c] = not isAttackable(r,c)

print(board)