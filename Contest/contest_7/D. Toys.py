

from collections import defaultdict

n,m = tuple(map(int, input().split()))

prices = list(map(int, input().split()))

andy_list = defaultdict(int)

for _ in range(m):
    andy_list[input()] += 1

prices.sort()

andy_list = dict(sorted(andy_list.items(), key=lambda item: item[1]))



min_ = 0
ptr = len(andy_list) -1

for items in andy_list.keys():
    min_ += prices[ptr] * andy_list[items]
    ptr -= 1

max_ = 0
ptr = n-len(andy_list)

for items in andy_list.keys():
    max_ += prices[ptr] * andy_list[items]
    ptr += 1

print(min_, max_)

