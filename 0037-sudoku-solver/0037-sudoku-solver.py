
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        rows = defaultdict(lambda: set())
        cols = defaultdict(lambda: set())
        subboxes = defaultdict(lambda: set())
        emptyBox = deque()

        # building the rows, cols, subboxes dictionary
        # plus holidng the empty spots in emptybox
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == ".":
                    emptyBox.appendleft((row,col))
                else:
                    rows[row].add(board[row][col])
                    cols[col].add(board[row][col])
                    subboxes[((3 * (row//3)), (col//3))].add(board[row][col])

        # print(subboxes)

        def solve():
            if len(emptyBox) == 0:
                return True

            row, col = emptyBox.pop()

            for num in map(str, range(1, 10)):
                if not (num in rows[row] or num in cols[col] or num in subboxes[((3 * (row//3)), (col//3))]):
                    board[row][col] = num
                    rows[row].add(num)
                    cols[col].add(num)
                    subboxes[((3 * (row//3)), (col//3))].add(num)

                    if solve():
                        return True

                    board[row][col] = "."
                    rows[row].remove(num)
                    cols[col].remove(num)
                    subboxes[((3 * (row//3)), (col//3))].remove(num)

            emptyBox.append((row, col))
            
            return False

        solve()

        """
        iterate once to hold the current dictionaries:
            row, column, subbox, emptyPositions(deque)

        backTrack:
            basecases:
                there are no emptyPositions: => solved, return true

                for each possibility in next empty space:
                    if its a valid number:
                        if backTrack:
                            return True

                return false i.e dead end
        """