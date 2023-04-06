

from collections import defaultdict


n = int(input())

adj_matrix = [list(map(int, input().split())) for _ in range(n)]
outgoing = defaultdict(list)

for row in range(n):
    for col in range(n):
        if adj_matrix[row][col] == 1:
            outgoing[row+1].append(col+1)


for i in range(1, n+1):
    print(len(outgoing[i]), *outgoing[i])

