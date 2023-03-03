class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = -1
        high = len(nums)

        while high > low+1:
            mid = (high+low)//2
            if nums[mid] < target:
                low = mid
            else:
                high = mid

        return 0 if low == -1 else low+1