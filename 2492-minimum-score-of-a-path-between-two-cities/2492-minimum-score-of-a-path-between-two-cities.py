class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        minRoadLength = defaultdict(lambda: float('inf'))
        treeDepth = {i:1 for i in range(1, n+1)}
        reps = {i:i for i in range(1, n+1)}

        def union(citya, cityb, roadLength):
            par1 = representative(citya)
            par2 = representative(cityb)
            newMin = min(minRoadLength[par1], minRoadLength[par2], roadLength)

            if par1 == par2:
                minRoadLength[par1] = newMin
                return


            if treeDepth[par1] > treeDepth[par2]:
                reps[par2] = par1
                treeDepth[par1] += treeDepth[par2]
                minRoadLength[par1] = newMin
            else:
                reps[par1] = par2
                treeDepth[par2] += treeDepth[par1]
                minRoadLength[par2] = newMin


        def representative(city) -> int:
            while reps[city] != city:
                city = reps[city]

            return city


        for citya, cityb, roadLength in roads:
            union(citya, cityb, roadLength)

        return minRoadLength[representative(1)]

