class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        new_nums = sorted(set(nums))
        
        for start in range(len(new_nums)):
            left = new_nums[start]
            right = left + n - 1
            pos = bisect_right(new_nums, right)
            remaining = n - (pos - start)
            ans = min(ans, remaining)

        return ans