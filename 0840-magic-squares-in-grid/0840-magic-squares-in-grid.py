class Solution(object):
    def isMagic(self, matrix, r, c):
        
        # check distnict
        items = []
        for row in range(r,r+3):
            for col in range(c,c+3):
                items.append(matrix[row][col])
        
        if len(items) != len(set(items)): return False
        for i in range(1,10):
            if i not in items:
                return False

        sums_ = []
            # row0, row1, row2
        rows = [[[0,0], [0,1], [0,2]], [[1,0],[1,1], [1,2]], [[2,0],[2,1],[2,2]]]
        cols = [[[0,0], [1,0], [2,0]], [[0,1],[1,1], [2,1]], [[0,2],[1,2],[2,2]]]
        diagonals = [[[0,0], [1,1], [2,2]], [[1,1],[2,0], [0,2]]]
        
        checkAll = [rows, cols, diagonals]

        for rows in checkAll:
            for row in rows:
                rowSum = 0
                for cell in row:
                    curr_row = cell[0] + r
                    curr_col = cell[1] + c
                    rowSum += matrix[curr_row][curr_col]
                sums_.append(rowSum)

        for index in range(len(sums_)-1):
            if sums_[index] != sums_[index+1]:
                return False

        return True


    def numMagicSquaresInside(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        
        numMagicSquares = 0
        for row in range(rows-2):
            for col in range(cols-2):
                if self.isMagic(grid, row, col):
                    numMagicSquares += 1
        
        return numMagicSquares

