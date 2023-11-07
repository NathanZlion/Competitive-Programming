from heapq import heappop, heappush

n, m = map(int, input().split())
r, c = map(int, input().split())
leftAllowed, rightAllowed = map(int, input().split())

reachable = [[False for _ in range(m)] for _ in range(n)]
reachable[r - 1][c - 1] = True  # starting r, c is reachable

laby = [input() for _ in range(n)]
pq = [(r - 1, c - 1, leftAllowed, rightAllowed)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = set()

def isInbound(r, c):
    return 0 <= r < n and 0 <= c < m

while pq:
    row, col, left, right = heappop(pq)
    if (row, col, left, right) in visited:
        continue

    visited.add((row, col, left, right))
    reachable[row][col] = True

    for rowDir, colDir in directions:
        if (not isInbound(row + rowDir, col + colDir)):
            continue

        if (laby[row][col] == '.') and (laby[row+rowDir][col+colDir] == '*'):
            continue
            
        # movving left
        if colDir == -1:
            if left > 0:
                heappush(pq, (row + rowDir, col+colDir, left-1, right))

        # moving right
        elif colDir == 1:
            if right > 0:
                heappush(pq, (row + rowDir, col+colDir, left, right-1))

        # moving up or down
        else:
            heappush(pq, (row + rowDir, col+colDir, left, right))

count = 0
for row in range(n):
    for col in range(m):
        if reachable[row][col]:
            count += 1

print(count)
