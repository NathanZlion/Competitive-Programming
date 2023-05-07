

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    res = arr[0]
    for num in arr:
        res&=num

    print(res)