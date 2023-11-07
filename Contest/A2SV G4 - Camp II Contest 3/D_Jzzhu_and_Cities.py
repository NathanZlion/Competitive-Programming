from collections import defaultdict
from math import inf
from heapq import heappop, heappush


numOfCities, numOfRoads, numOfTrains = map(int, input().split())
adjList = defaultdict(list)

# constructing the adjecency list
for _ in range(numOfRoads):
    u, v, roadLength = map(int, input().split())
    adjList[u-1].append((v-1, roadLength))


trainDist = []

for i in range(numOfTrains):
    city, routeLength = map(int, input().split())
    trainDist.append((city-1, roadLength))

minDist = [inf for _ in range(numOfCities)]

minDist[0] = 0 # start at the capital city
pq = [(0, 0)]

while pq:
    city, dist = heappop(pq)

    for neighbor, roadLength in adjList[city]:
        if minDist[neighbor] > dist + roadLength:
            minDist[neighbor] = dist + roadLength
            heappush(pq, (neighbor, minDist[neighbor]))

count = 0
for i in range(1, len(trainDist)):
    city, length = trainDist[i]
    if minDist[city] < length:
        count += 1

print(count)