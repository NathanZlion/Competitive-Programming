
from collections import defaultdict
from math import log, floor


t = int(input())

for _ in range(t):
    arrLen = int(input())
    arr = list(map(int, input().split()))
    freq = defaultdict(int)
    for num in arr:
        freq[floor(log(num, 2))] += 1
    
    res = 0
    for value in freq.values():
        res += ((value )* (value - 1)) // 2

    print(res)
