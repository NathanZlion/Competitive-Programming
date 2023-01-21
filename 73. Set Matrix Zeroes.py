class Solution(object):
    def setZeroes(self, matrix):
        row = len(matrix)
        col = len(matrix[0])

        zero_row = [0 for _ in range(col)]


        indices = []
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    indices.append([r,c])
        
        for zeros in indices:
            [rw,cl] = zeros
            matrix[rw] = zero_row
            for r in range(row):
                matrix[r][cl] = 0
                
        
