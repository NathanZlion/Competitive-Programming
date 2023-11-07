from collections import defaultdict


n, m, k = map(int, input().split())
arr = map(int, input().split())
operations = []
for _ in range(m):
    l, r, d = map(int, input().split())
    operations.append([l, r, d])

prefixSum = defaultdict(int)
for _ in range(k):
    x, y = map(int, input().split())
    prefixSum[x] += 1
    prefixSum[y+1] -= 1
