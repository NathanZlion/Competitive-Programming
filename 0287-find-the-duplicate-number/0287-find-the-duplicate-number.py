class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        def countLessThan(target):
            count = 0
            for num in nums:
                if num < target:
                    count += 1
            
            return count
        
        left = 0
        right = len(nums)
        
        while right > left +1:
            mid = left +  (right-left)//2

            if countLessThan(mid) > mid-1:
                right = mid
            else:
                left = mid
        
        return left

