class Solution:

    def search(self, nums, left, right):
        if left == right:
            return left
        
        mid = left + (right-left)//2
        if nums[mid] > nums[mid+1]:
            return self.search(nums, left, mid)
        return self.search(nums, mid+1, right)

    def findPeakElement(self, nums: List[int]) -> int:
        return self.search(nums, 0, len(nums)-1)
    