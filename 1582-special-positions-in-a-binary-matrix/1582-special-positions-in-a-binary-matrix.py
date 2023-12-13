class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_len = len(mat)
        col_len = len(mat[0])
        
        row_sum = defaultdict(int)
        col_sum = defaultdict(int)
        
        for row in range(row_len):
            for col in range(col_len):
                row_sum[row] += mat[row][col]
                col_sum[col] += mat[row][col]
        
        res = 0
        for row in range(row_len):
            for col in range(col_len):
                if (row_sum[row] == 1 and  col_sum[col] == 1 and mat[row][col] == 1):
                    res += 1
                    
        return res