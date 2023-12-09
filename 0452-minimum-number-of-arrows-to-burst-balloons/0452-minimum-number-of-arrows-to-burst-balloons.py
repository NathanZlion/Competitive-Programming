class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        num_of_arrows = 0
        for i in range(len(points)):
            points[i][1] *= -1
 
        heapify(points)
        while points:
            xstart, xend = heappop(points)
            xend *= -1
            
            while points:
                nextstart, nextend = points[0]
                nextend *= -1
                if nextstart > xend or nextend < xstart:
                    break

                xstart = max(xstart, nextstart)
                xend = min(xend, nextend)
                heappop(points)

            num_of_arrows += 1

        return num_of_arrows