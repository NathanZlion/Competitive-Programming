class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        overflow_memo = {}

        def overflow(row, col):
            if (row, col) in overflow_memo:
                return overflow_memo[(row, col)]
            
            # reached the top cup
            if row == 0 and col == 0:
                remaining : float = poured - 1.0
                if remaining > 0.0:
                    overflow_memo[(0, 0)] = remaining / 2
                else:
                    overflow_memo[(0, 0)] = 0.0

                return overflow_memo[(0, 0)]

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
            if row == 0 and col == 0:
                if poured >= 1:
                    return 1
                else:
                    return 0

            res = overflow(row - 1, col - 1) + overflow(row - 1, col)

            if res > 1:
                return 1

            return res
            

        return how_full(query_row, query_glass)
