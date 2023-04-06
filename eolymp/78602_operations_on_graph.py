

from collections import defaultdict


n = int(input())
adj_matrix = [list(map(int, input().split())) for _ in range(n)]

# sink: no outgoing edge
# source: no incoming edge

rows = defaultdict(int)
cols = defaultdict(int)

for row in range(n):
    for col in range(n):
        rows[row] += adj_matrix[row][col]
        cols[col] += adj_matrix[row][col]


sources = []
sinks = []

for row in rows:
    if rows[row] == 0:
        sinks.append(row+1)

for col in cols:
    if cols[col] == 0:
        sources.append(col+1)

sources.sort()
sinks.sort()


print(len(sources), *sources)
print(len(sinks), *sinks)
