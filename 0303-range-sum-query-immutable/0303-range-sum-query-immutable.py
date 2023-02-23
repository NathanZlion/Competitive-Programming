class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

        for i in range(1, len(nums)):
            self.nums[i] += self.nums[i-1]

    def sumRange(self, left: int, right: int) -> int:
        if not left:
            return self.nums[right]
        return self.nums[right] - self.nums[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)