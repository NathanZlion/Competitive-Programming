class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        rowLength = len(obstacleGrid)
        colLength = len(obstacleGrid[0])

        def isInbound(row, col):
            return 0 <= row and 0 <= col

        obstacleGrid[0][0] = -1

        for row in range(rowLength):
            for col in range(colLength):
                if obstacleGrid[row][col] == 1:
                    obstacleGrid[row][col] = 0
                    continue

                if isInbound(row -1, col):
                    obstacleGrid[row][col] += obstacleGrid[row -1][col]

                if isInbound(row, col-1):
                    obstacleGrid[row][col] += obstacleGrid[row][col-1]


        return -obstacleGrid[-1][-1]
