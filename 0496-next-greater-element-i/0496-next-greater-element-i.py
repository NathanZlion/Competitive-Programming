class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        'brute force approach'

        def no_exist():
            return -1

        dc = defaultdict(no_exist)
        m = len(nums2)

        for ptr1 in range(m):
            ptr2 = ptr1+1
            while ptr2 < m:
                if nums2[ptr2] > nums2[ptr1]:
                    dc[nums2[ptr1]] = nums2[ptr2]
                    break
                ptr2 += 1
        
        res = []
        for num in nums1:
            res.append(dc[num])
        
        return res

