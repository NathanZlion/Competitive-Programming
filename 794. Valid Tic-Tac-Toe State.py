class Solution(object):
    def checkWin(self, lst):
        WINNING_COMBINATIONS = [
            [0,1,2],
            [3,4,5],
            [6,7,8],
            [0,3,6],
            [1,4,7],
            [2,5,8],
            [0,4,8],
            [2,4,6],
        ]
        for combination in WINNING_COMBINATIONS:
            if all([(x in lst) for x in combination]):
                return True
        return False


    def validTicTacToe(self, board):
        X_COUNT = 0
        O_COUNT = 0

        x_indices = []
        o_indices = []
        for r, row in enumerate(board):
            for col in range(len(row)):
                char = row[col]
                if char == 'O':
                    O_COUNT += 1
                    o_indices.append(r*3+col)
                elif char == 'X':
                    X_COUNT += 1
                    x_indices.append(r*3+col)
        
        print(x_indices)
        print(o_indices)

        if X_COUNT < O_COUNT: return False
        if self.checkWin(x_indices) :
            if self.checkWin(o_indices):
                return False
            return X_COUNT == O_COUNT+1
        
        elif self.checkWin(o_indices):
            return X_COUNT == O_COUNT
        
        return X_COUNT <= O_COUNT +1

  
