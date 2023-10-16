class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[0 for _ in range(rowIndex+1)] for row in range(rowIndex+1)]
        for r in range(rowIndex+1):
            dp[r][0] = 1

        for row in range(1, rowIndex+1):
            for col in range(1, row+1):

                dp[row][col] = dp[row-1][col-1] + dp[row-1][col]

        return dp[rowIndex]