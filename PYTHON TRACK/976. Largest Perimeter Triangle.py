class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        currIdx = len(nums) - 1
        
        while currIdx >= 2:
            if (nums[currIdx - 2] + nums[currIdx - 1] > nums[currIdx]):
                return nums[currIdx] + nums[currIdx - 1] + nums[currIdx - 2]
            
            currIdx -= 1

        return 0
