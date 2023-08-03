class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        slow_ptr = 0
        for fast_ptr in range(len(nums)):
            if nums[fast_ptr] != 0:
                nums[slow_ptr], nums[fast_ptr] = nums[fast_ptr], nums[slow_ptr]
                slow_ptr += 1
