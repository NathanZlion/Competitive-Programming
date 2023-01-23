
n = int(input())

arr = list(map(int, input().split()))

arr.sort()

if arr[0] + arr[-2] > arr[-1]:
    print("YES")
    print(" ".join(list(map(str, arr))))

elif arr[-3] + arr[-2] > arr[-1]:
    arr[-1], arr[-2] = arr[-2], arr[-1]
    print("YES")
    print(" ".join(list(map(str, arr))))
else:
    print("NO")