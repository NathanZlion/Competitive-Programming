

n = int(input())

arr = list(map(int, input().split()))

a = 0
b = 0
max_ = 0
while a < n-1 and b < n-1:
    if arr[b] <= arr[b+1]:
        b+=1
    else:
        a = b+1
        b = a
    max_ = max(max_, b-a+1)
if not arr:
    print(0)
elif len(arr)==1:
    print(1)
else:
    print(max_)
