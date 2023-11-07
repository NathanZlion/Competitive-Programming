from collections import defaultdict

n = int(input())

edges = list(map(int, input().split()))
colors = list(map(int, input().split()))
adjList = defaultdict(list)

# construct the adjList
for index, vertex in enumerate(edges):
    index += 2
    adjList[min(index, vertex)].append(max(index, vertex))

stack = []
stack.append((1, 0))
numOfOperation = 0

while stack:
    nodeIndex, colorToPaint = stack.pop()
    if colorToPaint != colors[nodeIndex-1]:
        numOfOperation += 1
        colorToPaint = colors[nodeIndex-1]

    for childIndex in adjList[nodeIndex]:
        stack.append((childIndex, colorToPaint))

print(numOfOperation)
