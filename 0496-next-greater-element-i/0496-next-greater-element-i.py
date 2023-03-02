class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        'optimized monotonic stack approach'

        dc = defaultdict(lambda: -1)

        stack = []  # decreasing stack
        n = len(nums2)
        
        for index in range(n):
            while stack and stack[-1] < nums2[index]:
                dc[stack.pop()] = nums2[index]
            stack.append(nums2[index])
        
        res = []
        for num in nums1:
            res.append(dc[num])
        
        return res