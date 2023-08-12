class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # edge cases
        if 1 in [obstacleGrid[0][0], obstacleGrid[m-1][n-1]]:
            return 0

        # add padding to the right and bottom
        for row in obstacleGrid:
            row.append(0)
        obstacleGrid.append([0 for _ in range(n+1)])
        obstacleGrid[0][0] = 1

        for col in range(1, n):
            if obstacleGrid[0][col] == 1:
                obstacleGrid[0][col] = 0
            else:
                obstacleGrid[0][col] = obstacleGrid[0][col-1] + obstacleGrid[-1][col]

        for row in range(1, m):
            for col in range(n):
                if obstacleGrid[row][col] == 1:
                    obstacleGrid[row][col] = 0
                else:
                    obstacleGrid[row][col] = obstacleGrid[row-1][col] + obstacleGrid[row][col-1]


        return obstacleGrid[m-1][n-1]