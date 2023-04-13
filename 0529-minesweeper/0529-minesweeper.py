class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        directions = [(1,0),(0,1),(0,-1),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
        rowLength = len(board)
        colLength = len(board[0])
        
        def isInBound(row: int, col: int) -> bool:
            return 0 <= row < rowLength and \
                   0 <= col < colLength
        
        def mineNeighborCount(row: int, col: int) -> int:
            count = 0

            for r,c in directions:
                if isInBound(row+r, col+c):
                    count += 1 if board[row+r][col+c] == 'M' else 0

            return count

        def dfs(row: int, col: int)-> None:
            if board[row][col] == 'E':
                count = mineNeighborCount(row, col)

                if count > 0:
                    board[row][col] = str(count)

                else:
                    board[row][col] = 'B'
                    for r,c in directions:
                        if isInBound(row+r, col+c):
                            dfs(row+r, col+c)

        clickedRow, clickedCol = click

        if board[clickedRow][clickedCol] == "M":
            board[clickedRow][clickedCol] = "X"
            return board

        dfs(clickedRow, clickedCol)
        return board