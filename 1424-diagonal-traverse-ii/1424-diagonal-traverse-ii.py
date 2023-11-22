class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)
        row_len = len(nums)

        for row in range(row_len):
            for col, num in enumerate(nums[row]):
                diagonals[row + col].append(num)

        res = []
        for row_col_sum in sorted(diagonals.keys()):
            for num in diagonals[row_col_sum][::-1]:
                res.append(num)

        return res
