class Solution:
    def knightDialer(self, n: int) -> int:
        knight_jumps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
        non_numeric_cells = [(3, 0), (3, 2)]
        PHONE_PAD_ROWS = 4
        PHONE_PAD_COLS = 3
        modulus = (10**9 + 7)
        sys.setrecursionlimit(10005)

        def is_inbound(row, col):
            return 0 <= row < PHONE_PAD_ROWS and 0 <= col < PHONE_PAD_COLS

        @cache
        def possibilities(row, col, jumps_left):
            if (row, col) in non_numeric_cells or not is_inbound(row, col):
                return 0

            if jumps_left == 0:
                return 1

            res = 0
            for r, c in knight_jumps:
                res += possibilities(row + r, col + c, jumps_left -1)

            return res % modulus

        res = 0
        for row in range(4):
            for col in range(3):
                res += possibilities(row, col, n-1)

        return res % modulus
