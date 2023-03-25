class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)

        finished = False
        for index in range(n):
            while nums[index] != n and nums[index] != index:
                nums[nums[index]], nums[index] = nums[index], nums[nums[index]]

        for index in range(n):
            if index != nums[index]:
                return index

        return n
