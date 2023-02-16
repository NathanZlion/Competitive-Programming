

n,m = tuple(map(int, input().split()))

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

res = []

ptr1 = 0
ptr2 = 0

while ptr1 < n and ptr2 < m:
    if arr1[ptr1] > arr2[ptr2]:
        res.append(arr2[ptr2])
        ptr2 += 1
    else:
        res.append(arr1[ptr1])
        ptr1 += 1

while ptr2 < m:
        res.append(arr2[ptr2])
        ptr2 += 1
while ptr1 < n:
        res.append(arr1[ptr1])
        ptr1 += 1

print(*res)
