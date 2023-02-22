

m, n = tuple(map(int, input().split()))

arr_2 = list(map(int, input().split()))
arr_1 = list(map(int, input().split()))


res = []

arr2_idx = 0
for num in arr_1:

    while  arr2_idx < m and arr_2[arr2_idx] < num:
        arr2_idx +=1
    res.append(arr2_idx)

print(*res)
  

