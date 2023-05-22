class Solution:
    
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def manhattanDistance(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
        
        
        allEdges = []
        
        for i in range(len(points)-1):
            for j in range(i + 1, len(points)):
                point1, point2 = points[i], points[j]
                allEdges.append((manhattanDistance(point1, point2), tuple(point1), tuple(point2)))
        
        allEdges.sort()
        
        reps = {}
        
        def find(point):
            while point in reps:
                point = reps[point]
            
            return point

        def union(point1, point2):
            newRep = find(point2)

            while point1 in reps:
                nxt = reps[point1]
                reps[point1] = newRep
                point1 = nxt

            reps[point1] = newRep

        minimumCost = 0

        for edgeCost, point1, point2 in allEdges:
            if find(point1) != find(point2):
                union(point1, point2)
                minimumCost += edgeCost

        return minimumCost
                
                
                