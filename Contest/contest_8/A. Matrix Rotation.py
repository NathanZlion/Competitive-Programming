

t = int(input())

def rotate(arr):
    return [
        [arr[1][0], arr[0][0]]
        ,[arr[1][1], arr[0][1]]
    ]

def isBeautiful(arr):
    if (arr[0][0]>= arr[0][1]):
        return False
    if (arr[1][0]>= arr[1][1]):
        return False
    if (arr[0][0]>= arr[1][0]):
        return False
    if (arr[0][1]>= arr[1][1]):
        return False
    return True
    

for _ in range(t):
    arr = []
    arr.append(list(map(int, input().split())))
    arr.append(list(map(int, input().split())))

    beautiful = False

    for _ in range(4):
        if isBeautiful(arr):
            beautiful = True
            break
        arr = rotate(arr)
    
    if beautiful:
        print("YES")
    else:
        print("NO")
