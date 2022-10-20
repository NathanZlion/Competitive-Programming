class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        def dist(point):
            return ((point[0])**2 + (point[1])**2)

        def mergeSort(pointsArr):
            if len(pointsArr) > 1:
                leftHalf = pointsArr[: len(pointsArr) // 2]
                mergeSort(leftHalf)
                rightHalf = pointsArr[len(pointsArr) // 2 : ]
                mergeSort(rightHalf)
                merge(leftHalf,rightHalf,pointsArr)
            return pointsArr

        def merge(leftHalf,rightHalf,pointsArr):
            index1 = 0
            index2 = 0
            index3 = 0

            while(index1 < len(leftHalf) and index2 < len(rightHalf)):
                if(dist(leftHalf[index1]) < dist(rightHalf[index2])):
                    pointsArr[index3] = leftHalf[index1]
                    index1 += 1
                    index3 += 1
                else:
                    pointsArr[index3] = rightHalf[index2]
                    index2 += 1
                    index3 += 1
            if(index1 < len(leftHalf)):
                while(index1 < len(leftHalf)):
                    pointsArr[index3] = leftHalf[index1]
                    index1 += 1
                    index3 += 1
            else:
                while(index2 < len(rightHalf)):
                    pointsArr[index3] = rightHalf[index2]
                    index2 += 1
                    index3 += 1
        return (mergeSort(points)[:k])
