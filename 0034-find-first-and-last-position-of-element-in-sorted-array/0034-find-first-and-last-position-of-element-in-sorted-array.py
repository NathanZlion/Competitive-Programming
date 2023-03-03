class Solution:
    def startingPosition(self):
        low = -1
        high = len(self.nums)
        
        while high > low+1:
            mid = (high + low)//2
            if self.nums[mid] >= self.target:
                high = mid
            else:
                low = mid

        return -1 if high == len(self.nums) or self.nums[high] != self.target else high


    def endingPosition(self):
        low = -1
        high = len(self.nums)
        
        while high > low+1:
            mid = (high + low)//2
            if self.nums[mid] > self.target:
                high = mid
            else:
                low = mid

        return -1 if low == -1 or self.nums[low] != self.target else low
    

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target
        return [self.startingPosition(), self.endingPosition()]