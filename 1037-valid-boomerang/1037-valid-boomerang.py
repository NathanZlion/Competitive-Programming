class Solution:
    def getSlope(self, point1: List[int], point2: List[int]) -> float:
        x1, y1 = point1
        x2, y2 = point2
        
        if x1 == x2:
            return inf

        return (y2 - y1) / (x2 - x1)


    def areEqual(self, point1: List[int], point2: List[int]) -> float:
        x1, y1 = point1
        x2, y2 = point2

        return x1 == x2 and y1 == y2


    def isBoomerang(self, points: List[List[int]]) -> bool:
        points.sort(key = lambda coordinate: (coordinate[0], coordinate[1]))
        point1, point2, point3 = points
        
        if self.areEqual(point1, point2) or self.areEqual(point2, point3):
            return False

        return self.getSlope(point1, point2) != self.getSlope(point2, point3)
