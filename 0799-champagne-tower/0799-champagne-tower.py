class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        overflow_memo = {(-1, 0): poured}

        def overflow(row, col):
            if (row, col) in overflow_memo:
                return overflow_memo[(row, col)]

            # column becomes out of bound of tree
            if col < 0 or col > row:
                return 0.0

            curr_cup_poured = overflow(row - 1, col - 1) + overflow(row - 1, col)
            curr_cup_remaining =  curr_cup_poured - 1.0

            if curr_cup_remaining > 0:
                overflow_memo[(row, col)] = curr_cup_remaining / 2
            else:
                overflow_memo[(row, col)] = 0.0

            return overflow_memo[(row, col)]


        def how_full(row: int, col: int):
            res = overflow(row - 1, col - 1) + overflow(row - 1, col)

            if res > 1:
                return 1

            return res
            

        return how_full(query_row, query_glass)
