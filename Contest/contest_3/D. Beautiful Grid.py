

t = int(input())


def minimum_change(lst):
    # print(lst)
    res = 0
    for i in range(len(lst[0])-1):
        zeros = 0
        ones = 0
        for arr in lst:
            if arr[i] == "0":
                zeros += 1
            else:
                ones += 1
        
        res += min(zeros, ones)
    # print("res _" + str(res))
    return res


for _ in range(t):
    n = int(input())
    arr = []

    # construct an array of strings
    for _ in range(n):
        arr.append(input())
    
    col_left = 0
    col_right = len(arr[0])-1
    row_top = 0
    row_bottom = len(arr)-1

    changes = 0
    while col_left < col_right and row_top < row_bottom:
        arr_top = arr[row_top][col_left:col_right+1]
        arr_bottom = arr[row_bottom][col_left:col_right+1]

        arr_left = []
        for row in range(row_top, row_bottom+1):
            arr_left.append(arr[row][col_left])

        arr_right = []
        for row in range(row_top, row_bottom+1):
            arr_right.append(arr[row][col_right])
        
        changes += minimum_change([arr_left ,arr_right, list(arr_top), list(arr_bottom)])

        col_left += 1
        row_top += 1
        col_right -= 1
        row_bottom -= 1
    
    print(">>>" + str(changes))

