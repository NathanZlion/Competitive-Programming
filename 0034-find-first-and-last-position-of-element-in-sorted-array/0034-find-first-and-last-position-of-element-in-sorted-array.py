class Solution:
    @staticmethod
    def getPosition(nums: List[int], target: int, endPosition: bool) -> int:
        low = -1
        high = len(nums)

        while high > low+1:
            mid = (high + low)//2
            if (endPosition and nums[mid] > target) or ((not endPosition) and nums[mid] >= target):
                high = mid
            else:
                low = mid

        if endPosition:
            return -1 if (low == -1 or nums[low] != target) else low

        return -1 if (high == len(nums) or nums[high] != target) else high

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [Solution.getPosition(nums, target, False), Solution.getPosition(nums, target, True)]