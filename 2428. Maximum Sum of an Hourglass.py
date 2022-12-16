class Solution(object):
    def maxSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxSum = 0
        def hourGlassSum(x,y):
            return grid[x][y] + grid[x][y+1] + grid[x][y+2] + grid[x+1][y+1] + grid[x+2][y] + grid[x+2][y+1] + grid[x+2][y+2]

        for j in range(len(grid[0])-2):
            for i in range(len(grid)-2):
                maxSum = max(maxSum, hourGlassSum(i,j))
        return maxSum
