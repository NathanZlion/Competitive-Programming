class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)

        max_arith_seq_len = 0
        dp = {}

        for prev in range(len(nums)):
            for curr in range(prev + 1, len(nums)):
                diff = nums[curr] - nums[prev]

                if (prev, diff) in dp:
                    current_length = dp[(prev, diff)] + 1
                else:
                    current_length = 2

                dp[(curr, diff)] = current_length
                max_arith_seq_len = max(max_arith_seq_len, current_length)

        return max_arith_seq_len
