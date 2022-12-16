class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        def number(x):
            return int(x)
        nums.sort(key=number, reverse=True)
        return nums[k-1]
