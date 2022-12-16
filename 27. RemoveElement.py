
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ptr=0
        while ptr<len(nums):
            if nums[ptr]==val: nums.pop(ptr)
            else:
                ptr+=1
        return len(nums)
  
