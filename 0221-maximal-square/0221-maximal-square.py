class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0] * (cols+1) for _ in range(rows+1)]
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == "1":
                    r = row + 1
                    c = col + 1
                    dp[r][c] = min(dp[r][c-1], dp[r-1][c], dp[r-1][c-1]) + 1


        squareDimension = max([max(row) for row in dp])

        return squareDimension ** 2