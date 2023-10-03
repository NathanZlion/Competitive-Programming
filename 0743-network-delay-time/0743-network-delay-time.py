class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build adjList from weights.
        adjList = defaultdict(list)
        for u, v, w in times:
            adjList[u].append((w, v))

        minTimes = [inf for _ in range(n)]
        minTimes[k-1] = 0
        priorityQueue = [[0, k]]
        while priorityQueue:
            dist, node = heappop(priorityQueue)
            
            for weight, neighborNode in adjList[node]:
                if dist + weight < minTimes[neighborNode - 1]:
                    minTimes[neighborNode - 1] = dist + weight
                    heappush(priorityQueue, (dist + weight, neighborNode))

        minTimeToReachAll = max(minTimes)

        return -1 if minTimeToReachAll == inf else minTimeToReachAll