class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def isInbound(row, col):
            return 0 <= row < m and 0 <= col < n

        # starting with a 0 populated grid (matrix)
        res = [[0 for _ in range(n)] for _ in range(m)]

        res[0][0] = 1

        def getVal(row, col):
            if isInbound(row, col):
                return res[row][col]

            return 0

        for row in range(m):
            for col in range(n):
                # sum of direct left and direct up neighbor's moves
                res[row][col] += getVal(row-1, col) + getVal(row, col-1)


        return res[-1][-1]
