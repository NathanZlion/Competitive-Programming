

n = int(input())

arr = list(map(int, input().split()))

arr.sort()

if sum(arr[:n]) != sum(arr[n:]):
    print(*arr)
else:
    arr[0], arr[-1] = arr[-1], arr[0]

    if sum(arr[:n]) != sum(arr[n:]):
        print(*arr)
    else:
        print(-1)
