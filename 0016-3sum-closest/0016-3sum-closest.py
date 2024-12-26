class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closestSum = nums[0] + nums[1] + nums[2]
        length = len(nums)
        
        for left in range(length - 2):
            mid = left + 1
            right = length - 1
            
            while right > mid:
                currSum = nums[left] + nums[mid] + nums[right]
                
                # distance from the target sum
                closestSum = min(closestSum, currSum, key=lambda k: abs(target - k))
                
                if currSum > target:
                    right -= 1
                else:
                    mid += 1
            
        return closestSum
