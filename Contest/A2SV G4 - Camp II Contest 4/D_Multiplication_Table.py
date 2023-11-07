from heapq import heappop, heappush

n, m, k = map(int, input().split())

heap = [(1, 1)]
for _ in range(k - 1):
    i, j = heappop(heap)
    heappush(heap, (i + 1, j))
    heappush(heap, (i, j + 1))
    heappush(heap, (i + 1, j + 1))


i, j = heappop(heap)
print(i * j)