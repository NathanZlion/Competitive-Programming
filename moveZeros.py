class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) == 0 or len(nums) ==1:
            return

        pointer = 0
        lastIndex = len(nums) -1

        while pointer < lastIndex:
            if nums[pointer] == 0:
                nums.pop(pointer)
                nums.append(0)
                lastIndex -= 1
            else:
                pointer += 1
