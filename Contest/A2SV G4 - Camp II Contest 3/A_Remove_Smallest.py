
t = int(input())

def canRemove(arr):
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] > 1:
            return False
    
    return True

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if canRemove(arr):
        print("YES")
    else:
        print("NO")