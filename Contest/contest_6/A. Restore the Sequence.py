

t = int(input())

for _ in range(t):
    n = int(input())

    arr = list(map(int, input().split()))

    ptr1 = 0
    ptr2 = n-1

    res = []
    while ptr2 >= ptr1:
        res.append(arr[ptr1])
        res.append(arr[ptr2])
        ptr1 += 1
        ptr2 -= 1
    
    if (n % 2):
        res.pop()
    
    print(*res)


