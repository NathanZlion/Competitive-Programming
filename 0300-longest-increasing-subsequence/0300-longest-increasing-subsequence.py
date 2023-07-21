class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # from right to left: calculate the maximum
        inc_sequence = [1] * len(nums)

        for left in range(len(nums)-1, -1, -1):
            for right in range(left + 1, len(nums)):
                if nums[right] > nums[left]:
                    inc_sequence[left] = max(inc_sequence[left], 1 + inc_sequence[right])

        return max(inc_sequence)
