class Solution:
    def reductionOperations(self, nums: List[int]) -> int:

        nums = Counter(nums)
        nums = [(num, count) for num, count in nums.items()]

        operations_count = 0
        val_count = 0

        nums.sort()
        for index in range(len(nums)-1, 0, -1):
            cur_num, cur_count = nums[index]
            val_count += cur_count
            operations_count += val_count

        return operations_count
