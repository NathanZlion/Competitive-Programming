class Solution(object):

    def checkdistnict(self, lst):
        res = []
        for num in lst:
            if num != ".":
                res.append(num)
        
        return len(res) == len(set(res))
    

    def isValidSudoku(self, board):
        # checkRows
        for row in board:
            if not self.checkdistnict(row):
                print(row)
                print(set(row))
                print("fail 0")
                return False
        
        # checkCols
        cols = defaultdict(list)
        for row in board:
            for col in range(9):
                cols[col].append(row[col])
        
        print(cols)
        for c in cols:
            if not self.checkdistnict(cols[c]):
                print("fail 1")
                return False
        
        # [start, end]
        partitions = [
            [0,3],
            [3,6],
            [6,9],
        ]

        for row in partitions:
            for col in partitions:
                subBox = []
                for r in range(row[0], row[1]):
                    for c in range(col[0],col[1]):
                        subBox.append(board[r][c])

                if not self.checkdistnict(subBox):
                    return False
        
        return True

        
