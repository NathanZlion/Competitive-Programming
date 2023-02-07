

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    found = False
    for i in range(n-1):
        if arr[i+1]-arr[i] >1:
            print("NO")
            found = True
            break

    if not found:
        print("YES")
