class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        memo = {}

        def canPartitionFromIndex(index) -> bool:
            if index in memo:
                return memo[index]
            
            if index == len(nums):
                return True
            
            if index > len(nums):
                return False

            # the three patterns
            if index <= len(nums) - 2 and nums[index] == nums[index+1]:
                if canPartitionFromIndex(index+2):
                    return True

            if index <= len(nums) - 3 and nums[index] == nums[index+1] == nums[index+2]:
                if canPartitionFromIndex(index+3):
                    return True

            if index <= len(nums) - 3 and (nums[index]+1==nums[index+1] and nums[index+1]+1==nums[index+2]):
                if canPartitionFromIndex(index+3):
                    return True

            memo[index] = False
            return False

        return canPartitionFromIndex(0)