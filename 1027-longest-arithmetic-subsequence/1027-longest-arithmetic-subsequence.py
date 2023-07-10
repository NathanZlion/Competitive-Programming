class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)

        max_arith_seq_len = 0
        dp = {}

        for prev in range(len(nums)):
            for curr in range(prev + 1, len(nums)):
                diff = nums[curr] - nums[prev]
                current_length = dp[(prev, diff)] if (prev, diff) in dp else 1
                current_length += 1   # accounts for curr added to sequence
                dp[(curr, diff)] = current_length
                max_arith_seq_len = max(max_arith_seq_len, current_length)

        return max_arith_seq_len
