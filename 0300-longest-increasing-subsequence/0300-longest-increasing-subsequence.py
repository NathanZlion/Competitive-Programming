from math import inf

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.N = len(nums)
        nums.append(-inf)

        @cache
        def dp(index: int) -> int:
            res = 1

            for nextIndex in range(index+1, self.N):
                if nums[index] < nums[nextIndex]:
                    res = max(res, 1 + dp(nextIndex))
                
            return res
        
        return dp(-1) - 1
    