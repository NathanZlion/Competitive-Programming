t = int(input())
 
for _ in range(t):
    a, b = list(map(int,input().split()))
 
    left = -1
    right = (a+b)//4 + 1
 
    while left + 1 < right:
        mid = left + (right - left)// 2
 
        if mid > min(a, b):
            right = mid
        else:
            left = mid
 
    print(left)
