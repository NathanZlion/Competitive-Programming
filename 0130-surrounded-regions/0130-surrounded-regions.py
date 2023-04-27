class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        """
        - flood it from the borders and change the explored O s to an intermediate 'Y' 
        - Then final traverse once to change all  Y => O and O => X
        """
        numberOfRows = len(board)
        numberOfCols = len(board[0])

        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

        def isInbound(row, col):
            return 0 <= row < numberOfRows and 0 <= col < numberOfCols
        
        def dfs(row, col):
            # changes all reachable 'O' from this row to 'Y'

            for r, c in directions:
                if isInbound(row+r, col+c) and board[row+r][col+c] == "O":
                    board[row+r][col+c] = "Y"
                    dfs(row+r, col+c)

        # upper row and last row
        for col in range(numberOfCols):
            if  board[0][col] == "O": # upper row
                board[0][col] = "Y"
                dfs(0, col)

            if board[numberOfRows - 1][col] == "O": # last row
                board[numberOfRows - 1][col] = "Y"
                dfs(numberOfRows - 1, col)

        # left most col and right most col
        for row in range(numberOfRows):
            if  board[row][0] == "O": # left col
                board[row][0] = "Y"
                dfs(row, 0)

            if board[row][numberOfCols - 1] == "O": # right most col
                board[row][numberOfCols - 1] = "Y"
                dfs(row, numberOfCols - 1)


        for row in range(numberOfRows):
            for col in range(numberOfCols):
                if board[row][col] == "Y":
                    board[row][col] = "O"
                
                elif board[row][col] == "O":
                    board[row][col] = "X"
        
            
        