

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    count = 0
    arr.sort()

    arr.append(0)

    left = -1
    for right in range(n):
        while right > left and arr[left]&arr[right] < arr[left]^arr[right]:
            left += 1
        count += (right - left)
        
    print(count)
