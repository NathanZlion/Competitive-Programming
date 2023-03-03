class Solution:
    def startingPosition(self, nums, target):
        '''
        low  => num < target
        high => num >= target
        '''
        low = -1
        high = len(nums)
        
        while high > low+1:
            mid = (high + low)//2
            if nums[mid] >= target:
                high = mid
            else:
                low = mid

        return -1 if high == len(nums) or nums[high]!=target else high


    def endingPosition(self, nums, target):
        '''
        low  => num <= target
        high => num > target
        '''
        low = -1
        high = len(nums)
        
        while high > low+1:
            mid = (high + low)//2
            if nums[mid] > target:
                high = mid
            else:
                low = mid

        return -1 if low == -1 or nums[low] != target else low
    

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.startingPosition(nums, target), self.endingPosition(nums, target)]