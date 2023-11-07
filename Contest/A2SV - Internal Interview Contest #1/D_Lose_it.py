n = int(input())
arr = map(int, input().split())
index = {4: 0, 8: 1, 15: 2, 16: 3, 23: 4, 42: 5}
count = [0 for _ in range(6)]

res = 0
for num in arr:
    idx = index[num]
    minCount = count[idx]+1
    for i in range(idx):
        minCount = min(minCount, count[i])

    if minCount > count[idx]:
        count[idx] += 1
    else:
        res += 1
    
minCount = min(count)
for count_ in count:
    res += (count_ - minCount)

print(res)