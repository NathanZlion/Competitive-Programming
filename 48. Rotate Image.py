class Solution(object):
    def rotate(self, matrix):
    
        n = len(matrix)
        dupMatrix = []
        for row in matrix:
            r = []
            for c in row:
                r.append(c)
            dupMatrix.append(r)


        for row in range(n):
            for col in range(n):
                matrix[row][col] = dupMatrix[n - col - 1][row]
