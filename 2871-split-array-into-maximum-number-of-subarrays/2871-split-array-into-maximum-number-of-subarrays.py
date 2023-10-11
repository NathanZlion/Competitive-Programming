class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        runningAnd = 2 ** 30 - 1

        for num in nums:
            runningAnd &= num

        if runningAnd != 0:
            return 1

        count = 0
        runningAnd = 2 ** 30 - 1

        for index in range(len(nums)):
            num = nums[index]
            runningAnd &= num

            if runningAnd == 0:
                count += 1

                if index < len(nums)-1:
                    runningAnd = nums[index+1]
                else:
                    break

        return count