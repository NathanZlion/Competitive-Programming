

n,k = list(map(int, input().split()))
arr = list(map(int, input().split()))

arr.sort()
if k == 0:
    if arr[0] > 1:
        print(1)
    else:
        print(-1)
        
elif k == n:
    if arr[-1] <= 10**9:
        print(arr[-1])
    else:
        print(-1)

elif k > n:
    print(-1)

else:

    if arr[k-1] == arr[k]:
        print(-1)
    else:
        print(arr[k-1])
