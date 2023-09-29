class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return sorted(nums) == nums or sorted(nums, reverse=True) == nums