class Solution:
    def knightDialer(self, n: int) -> int:
        modulus = (10**9 + 7)
        knight_jumps = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }

        @cache
        def possibilities(curr_cell, jumps_left):
            if jumps_left == 0:
                return 1

            res = 0
            for next_cell in knight_jumps[curr_cell]:
                res += possibilities(next_cell, jumps_left -1)

            return res % modulus

        res = 0
        for curr_cell in range(10):
            res += possibilities(curr_cell, n-1)

        return res % modulus