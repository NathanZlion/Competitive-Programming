
t = int(input())

def minimum_change(indexes, arr):
    zeros = 0
    ones = 0
    for index in indexes:
        if arr[index[0]][index[1]] == 0:
            zeros += 1
        else:
            ones += 1
    return min(zeros, ones)

def transformations(row, col, n):
    return [[row,col],[col,n-row-1],[n-row-1,n-col-1],[n-col-1,row]]

for _ in range(t):
    n = int(input())

    # construct an array of integers
    r = []
    for _ in range(n):
        r.append(input())
    
    arr = []
    for row in r:
        newR = []
        for char in row:
            newR.append(int(char))
        arr.append(newR)
    
    col_left = 0
    col_right = len(arr[0])-1

    changes = 0
    for row in range(n//2):
        for col in range(col_left, col_right):
            changes+=minimum_change(transformations(row,col,n), arr)

        col_left += 1
        col_right -= 1


    print(changes)
