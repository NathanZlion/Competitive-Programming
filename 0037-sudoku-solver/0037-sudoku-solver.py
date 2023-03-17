
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def check(row: int, col: int, digit: str) -> bool:
            # check if there's no duplicate in that column
            for c in range(9):
                if c != col and board[row][c] == digit:
                    return False
                            
            # check if there's no duplicate in that row
            for r in range(9):
                if r != row and board[r][col] == digit:
                    return False
            
            # check if there's no duplicate in that specific 3X3 sub box
            rowStart, colStart = row - (row%3), col - (col%3)

            for r in range(rowStart, rowStart+3):
                for c in range(colStart, colStart+3):
                    if (r != row) and (c != col) and (board[r][c] == digit): 
                        return False

            return True

        
        def solve(row, col) -> bool:

            row += (col // 9)
            col %= 9

            # find the next empty space in the board            
            while row < 9:
                if board[row][col] == '.':
                    break
                col += 1
                row += (col // 9)
                col %= 9

            # finished solving
            if  row > 8:
                return True

            # try out valid placeholders in it and backTrack
            for digit in range(1,10):

                if check(row, col, str(digit)):
                    board[row][col] = str(digit)

                    if solve(row, col+1):
                        return True

                    board[row][col] = '.'

            return False

        solve(0, 0)