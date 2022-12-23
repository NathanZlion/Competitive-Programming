class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """

        from math import fabs

        index = -1
        curr_dce = 9999999

        def y_dce(point):
            return fabs(point[1] -y)

        def x_dce(point):
            return fabs(point[0]-x)

        def isValid(point):
            return ((point[0] == x) or (point[1] == y))

        for idx, point in enumerate(points):
            if (point[0] == x):
                if y_dce(point) < curr_dce:
                    index = idx
                    curr_dce = y_dce(point)

            elif (point[1] == y):
                if x_dce(point) < curr_dce:
                    index = idx
                    curr_dce = x_dce(point)

        return index
