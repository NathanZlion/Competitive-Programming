class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # optimize the runtime.
        n = len(nums)

        left = -1
        k = 0
        maxSize = 0

        for right in range(n):
            if nums[right] == 0:
                k += 1

            # there is a 0 inside this subarray, delete that with the left one
            if k != 0:
                while k > 1:
                    left += 1
                    if nums[left] == 0:
                        k -= 1

                maxSize = max(maxSize, right - left - k)

            # delete a 1 from the subarray
            else:
                maxSize = max(maxSize, right - left - 1)

        return maxSize
