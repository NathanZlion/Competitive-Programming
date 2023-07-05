class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        left = -1
        n = len(nums)
        k = 0
        maxSize = 0
        
        for right in range(n):
            if nums[right] == 0:
                k += 1

            if k != 0:
                while k > 1:
                    left += 1
                    if nums[left] == 0:
                        k -= 1

                maxSize = max(maxSize, right - left - k)

            else:
                maxSize = max(maxSize, right - left - 1)
        
        return maxSize