class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        row_len = len(matrix)
        col_len = len(matrix[0])
        ans = 0

        for row in range(row_len):
            for col in range(col_len):
                if matrix[row][col] != 0 and row > 0:
                    matrix[row][col] += matrix[row - 1][col]

            curr_row = sorted(matrix[row], reverse=True)
            for i in range(col_len):
                ans = max(ans, curr_row[i] * (i + 1))

        return ans