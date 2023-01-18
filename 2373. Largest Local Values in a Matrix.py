class Solution(object):

    def findMax(self, row, col, grid):
        max_ = grid[row][col]
        pattern = [[0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]
        for dp in pattern:
            newrow = row + dp[0]
            newcol = col + dp[1]
            max_ = max(max_, grid[newrow][newcol])
        
        return max_


    def largestLocal(self, grid):
        n = len(grid)

        res = [[0 for i in range(n-2)] for _ in range(n-2)]

        for row in range(len(res)):
            for col in range(len(res[0])):
                res[row][col] = max(res[row][col], self.findMax(row, col, grid))


        return res
