
from heapq import heapify, heappop, heappush

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    whiteboard = list(map(int, input().split()))   # n boards
    operations = list(map(int, input().split()))    # m operations

    # change the m smallest whiteboard contents  
    heapify(whiteboard)

    for operation in operations:
        heappop(whiteboard)
        heappush(whiteboard, operation)

    print(sum(whiteboard))
