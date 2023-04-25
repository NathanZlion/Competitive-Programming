
n = int(input())
ax, ay = map(int, input().split()) # alice
bx, by = map(int, input().split()) # bob
cx, cy = map(int, input().split()) # destination

arow, acol = ay-1, ax-1
brow, bcol = by-1, bx-1
crow, ccol = cy-1, cx-1

board = [[True for _ in range(n+1)] for _ in range(n+1)]

directions = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(1,1),(1,-1),(-1,1)]

def isAttackable(row, col):
    return row == arow or col == acol or abs(row-arow)==abs(col-acol)

def isInbound(row, col):
    return 0 <= row < n and 0 <= col < n

for r in range(n):
    for c in range(n):
        board[r][c] = not isAttackable(r,c)

def dfs(row, col) -> bool:
    if row == crow and col == ccol:
        return True

    board[row][col] = False

    for r, c in directions:
        if isInbound(row+r, col+c):
            if board[row+r][col+c] == True:
                if dfs(row+r, col+c):
                    return True

    return False


print("YES" if dfs(brow, bcol) else "NO")

