class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
        -> there has to be a queen in every row of the board.
        -> enumerate every possible position, while not violating the rule.
        '''
        
        def makeString(lst: List[List[int]]) -> List[str]:
            res = []
            for row in lst:
                res.append("".join(row))
            return res


        def isValid(row, col):

            # check column wise up
            for r in range(row):
                if r != row and currState[r][col] == 'Q':
                    return False
            
            # check diagonal top left
            r,c = row-1, col-1

            while r > -1 and c > -1:
                if currState[r][c] == 'Q':
                    return False
                r -= 1
                c -= 1

            # check diagonal top right
            r,c = row-1, col+1
            while r > -1 and c < n:
                if currState[r][c] == 'Q':
                    return False
                r -= 1
                c += 1

            return True


        currState = [['.' for _ in range(n)] for _ in range(n)]
        solution = []
        self.combinations = []

        def backTrack(row):
            if row == n:
                self.combinations.append(makeString(currState))
                return

            for col in range(n):
                if isValid(row, col):
                    currState[row][col] = 'Q'
                    backTrack(row+1)
                    currState[row][col] = '.'

        backTrack(0)
        
        return self.combinations
        
        