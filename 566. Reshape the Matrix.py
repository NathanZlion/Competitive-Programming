class Solution(object):
    def matrixReshape(self, mat, r, c):
   
        rows = len(mat)
        cols = len(mat[0])

        if rows * cols != r * c:
            return mat
        
        lst = []
        for row in mat:
            for col in row:
                lst.append(col)
        
        res_mat = [[0 for _ in range(c)] for _ in range(r)]

        for row in range(r-1,-1,-1):
            for col in range(c-1, -1, -1):
                res_mat[row][col] = lst.pop()

        
        return res_mat        
