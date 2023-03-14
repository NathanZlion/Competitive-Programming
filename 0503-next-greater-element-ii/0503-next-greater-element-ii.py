class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        stack = []
        ans = [-1 for _ in range(len(nums))]
        
        for index in range(2* len(nums)):
            index %= len(nums)

            while stack and nums[stack[-1]] < nums[index]:
                ans[stack.pop()] = nums[index]
            
            stack.append(index)


        return ans