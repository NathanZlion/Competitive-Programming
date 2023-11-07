from collections import defaultdict

t = int(input())

for _ in range(t):
    arrLen = int(input())
    arr = list(map(int, list(input())))
    for i in range(len(arr)):
        arr[i] -= 1

    res = runningSum = 0
    freq = defaultdict(int)
    freq[0] = 1
    for num in arr:
        runningSum += num
        res += freq[runningSum]
        freq[runningSum] += 1

    print(res)
