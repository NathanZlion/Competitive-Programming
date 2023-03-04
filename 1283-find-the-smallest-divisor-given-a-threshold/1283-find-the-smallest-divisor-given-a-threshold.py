class Solution:
    
    def divideAndAdd(self, nums: List[int], divisor: int) -> int:
        sum_ = 0

        for num in nums:
            sum_ += ceil(num/divisor)
        
        return sum_


    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        low = 0
        high = max(nums)+1
        
        while high > low+1:
            mid = low + (high - low)//2
            if self.divideAndAdd(nums, mid) > threshold:
                low = mid
            else:
                high = mid
        
        return high
