class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0

        for left, value in enumerate(nums):
            for right in range(left+1, len(nums)):
                if nums[right] ==value:
                    res+=1

        return res
