class Solution:
    def totalNQueens(self, n: int) -> int:
        '''
        -> there has to be a queen in every row of the board.
        -> enumerate every possible position, while not violating the rule.
        '''

        def isValid(row, col):

            # check column
            for r in range(row):
                if r != row and currState[r][col] == 1:
                    return False
            
            # check diagonal top left
            
            r,c = row-1, col-1
            
            while r > -1 and c > -1:
                if currState[r][c] == 1:
                    return False
                r -= 1
                c -= 1

        

            # check diagonal top right
            
            r,c = row-1, col+1
            
            while r > -1 and c < n:
                if currState[r][c] == 1:
                    return False
                r -= 1
                c += 1

            return True
            
            
        currState = [[0 for _ in range(n)] for _ in range(n)]
        solution = []
        self.totalCount = 0

        def backTrack(row):
            if row == n:
                self.totalCount += 1
                return

            for col in range(n):
                if isValid(row, col):
                    currState[row][col] = 1
                    backTrack(row+1)
                    currState[row][col] = 0

        backTrack(0)
        
        return self.totalCount
        
        