

t = int(input())

# brute force approach
"""
check diagonal sum for every cell
"""


def diag_sum(arr, row, col, n, m):

    d_sum = arr[row][col]

    # move top left
    i,j = row, col
    while i>0 and j>0:
        i-=1
        j-=1
        d_sum += arr[i][j]

    # move top right
    i,j = row, col
    while i>0 and j<m-1:
        i-=1
        j+=1
        d_sum += arr[i][j]
    
    # move bottom right
    i,j = row, col
    while i<n-1 and j<m-1:
        i+=1
        j+=1
        d_sum += arr[i][j]

    # move bottom left
    i,j = row, col
    while i<n-1 and j>0:
        i+=1
        j-=1
        d_sum += arr[i][j]
    
    return d_sum


for _ in range(t):
    n, m =  tuple(map(int, input().split()))

    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))


    max_diag_sum = 0
    for r_idx in range(n):
        for c_idx in range(m):
            max_diag_sum = max(max_diag_sum, diag_sum(arr, r_idx, c_idx, n ,m))
    
    print(max_diag_sum)
