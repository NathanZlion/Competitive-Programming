class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.length = len(word)
        self.board_row_size, self.board_col_size = len(board), len(board[0])
        self.neighbours = [(-1,0),(1,0),(0,-1),(0,1)]

        def word_search(row, col, index):
            if index == self.length:
                return True

            if (row == self.board_row_size or col == self.board_col_size or
                row < 0 or col < 0 or board[row][col] != word[index]):
                return False

            temp = board[row][col]
            board[row][col] = "#"

            # traverse its neighbors
            for neighbour in self.neighbours:
                if word_search(row + neighbour[0], col + neighbour[1], index+1):
                    return True

            board[row][col] = temp
            return False

        for row in range(self.board_row_size):
            for col in range(self.board_col_size):
                if board[row][col] == word[0] and word_search(row, col, 0):
                    return True

        return False
