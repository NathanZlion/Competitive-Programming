class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_ptr = 0
        n = len(nums)

        for nonzero_ptr in range(n):
            if nums[nonzero_ptr] != 0:
                nums[nonzero_ptr], nums[zero_ptr] = nums[zero_ptr], nums[nonzero_ptr]

            while zero_ptr <= nonzero_ptr and nums[zero_ptr] != 0:
                zero_ptr += 1