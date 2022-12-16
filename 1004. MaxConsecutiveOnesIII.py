class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        maxLength = 0

        for index, num in enumerate(nums):
            k -= (1-num)
            if k < 0:
                k += (1 - nums[left])
                left += 1
            
            currWindowSize = index - left +1
            if maxLength < currWindowSize:
                maxLength = currWindowSize
        return maxLength
