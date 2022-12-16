class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        indices = []
        index=0
        for num in nums:
            if num == target:
                indices.append(index)
            index+=1
        return indices
