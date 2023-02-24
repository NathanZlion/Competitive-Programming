class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        greater = [-1 for _ in range(len(nums2))]

        for index in range(len(nums2)-1, -1, -1):
            num = nums2[index]
            while stack and stack[-1] <= num:
                stack.pop()
            
            if stack:
                greater[index] = stack[-1]
            
            stack.append(num)
        
        dc = {}
        for index in range(len(nums2)):
            dc[nums2[index]] = greater[index]
        
        res = []
        for num in nums1:
            res.append(dc[num])
        
        return res
                
                
            
