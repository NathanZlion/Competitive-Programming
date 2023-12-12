class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row_len = len(matrix)
        col_len = len(matrix[0])
        res_matrix = [[0 for _ in range(row_len)] for _ in range(col_len)]

        for row in range(row_len):
            for col in range(col_len):
                res_matrix[col][row] = matrix[row][col]

        return res_matrix