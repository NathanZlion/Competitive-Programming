class Solution(object):
    def traverse(self, matrix, row_top, row_bottom, col_left, col_right):
        sum_ = []
        sum_.extend(matrix[row_top][col_left: col_right+1])

        for row in range(row_top+1, row_bottom+1):
            sum_.append(matrix[row][col_right])

        sum_.extend((matrix[row_bottom][col_left+1:col_right])[::-1])

        for row in range(row_bottom, row_top, -1):
            sum_.append(matrix[row][col_left])

        return sum_


    def spiralOrder(self, matrix):
        if not matrix:
            return matrix

        res = []
        row_top = 0
        row_bottom = len(matrix)-1
        col_left = 0
        col_right = len(matrix[0])-1

        while row_top <= row_bottom and col_left <= col_right:
            res.extend(self.traverse(matrix, row_top, row_bottom, col_left, col_right))
            row_bottom -= 1
            row_top += 1
            col_left += 1
            col_right -= 1

        while len(res) > len(matrix)*len(matrix[0]):
            res.pop()

        return res
                
