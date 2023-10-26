class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = 1
        n = len(nums)
        left = 0
        max_window_size = 0

        for right in range(n):
            if nums[right] == 0:
                k -= 1

            while k < 0:
                if nums[left] == 0:
                    k += 1

                left += 1

            max_window_size = max(max_window_size, right - left)

        return max_window_size
