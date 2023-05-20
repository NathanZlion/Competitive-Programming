class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res = []
        ptr1 = 0
        ptr2 = 0
        
        while ptr1 < len(nums1) and ptr2 < len(nums2):
            if nums1[ptr1] < nums2[ptr2]:
                ptr1 += 1
            
            elif nums1[ptr1] > nums2[ptr2]:
                ptr2 += 1
        
            else:
                res.append(nums1[ptr1])
                ptr1 += 1
                ptr2 += 1
                
        return res
                
            