class Solution(object):
    def maxSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxSum = 0
        dirs = [[0,0],[0,1],[0,2],[1,1],[2,0],[2,1],[2,2]]
        def hourGlassSum(x,y):
            acc = 0
            for [dx, dy] in dirs:
                newRow = dx +x
                newCol = dy +y
                acc += grid[newRow][newCol]
            return acc

        for j in range(len(grid[0])-2):
            for i in range(len(grid)-2):
                maxSum = max(maxSum, hourGlassSum(i,j))
        return maxSum


