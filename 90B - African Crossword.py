
n,m = tuple(map(int, input().split()))
 
"""
cross out all repeating letters and return original word
"""

def checkMatches(row, col, arr):
    val = arr[row][col]
 
    # at the row
    for c in range(len(arr[0])):
        if c != col and (arr[row][c] == val):
            return True
 
    # at the column
    for r in range(len(arr)):
        if r != row and (arr[r][col] == val):
            return True
    
    return False
 
 
crossedOut = [[False for i in range(m)] for j in range(n)]
 
crossWord = []
for _ in range(n):
    i = input()
    row = []
    for c in range(len(i)):
        row.append(i[c])
    crossWord.append(row)
        
for row in range(n):
    for col in range(m):
        if checkMatches(row, col, crossWord):
            crossedOut[row][col] = True
 
 
res = []
for row in range(n):
    for col in range(m):
        if not crossedOut[row][col]:
            res.append(crossWord[row][col])
 
 
print("".join(res))
