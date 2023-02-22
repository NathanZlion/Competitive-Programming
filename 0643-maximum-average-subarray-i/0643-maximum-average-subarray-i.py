class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        sum_ = sum(nums[:k])
        max_sum = sum_
        
        n = len(nums)
        for i in range(k,n):
            sum_ += nums[i]
            sum_ -= nums[i-k]
            max_sum = max(sum_, max_sum)            
        
        return max_sum/k
                
