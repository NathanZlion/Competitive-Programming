class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        # {number: index in nums}
        nums_hash = {}
        
        for index in range(len(nums)):
            nums_hash[nums[index]] = index
        
        for operation in operations:
            # find index of the number to replace from nums_hash
            curr_index = nums_hash[operation[0]]
            
            # delete that and assign that index to the new number in operation[1]
            del nums_hash[operation[0]]
            nums_hash[operation[1]] = curr_index
        
        # update nums with replacements
        for num in nums_hash:
            nums[nums_hash[num]] = num
        
        return nums
