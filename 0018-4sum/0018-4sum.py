class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        length = len(nums)
        nums.sort()
        
        visitedPtr1 = set()
        
        for ptr1 in range(length - 3):
            if ptr1 in visitedPtr1:
                continue
            
            visitedPtr1.add(ptr1)
            targetSum = target - nums[ptr1]
            for left in range(ptr1 + 1, length - 2):
                mid = left + 1
                right = length - 1
                
                while right > mid:
                    _sum = nums[left] + nums[mid] + nums[right]
                    
                    if _sum > targetSum:
                        right -= 1
                    elif _sum < targetSum:
                        mid += 1
                    else:
                        res.add(
                            (
                                nums[ptr1],
                                nums[left],
                                nums[mid],
                                nums[right]
                            )
                        )
                        mid += 1
                        
        return list(res)
    