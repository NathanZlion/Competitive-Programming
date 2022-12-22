class Solution(object):
    def merge(self, nums1, m, nums2, n):
        res=[]
        ptr1=0
        ptr2=0

        while ptr1<m and ptr2<n:
            if nums1[ptr1] <= nums2[ptr2]:
                res.append(nums1[ptr1])
                ptr1 += 1
            else:
                res.append(nums2[ptr2])
                ptr2 += 1

        while ptr1 < m:
            res.append(nums1[ptr1])
            ptr1 += 1

        while ptr2 < n:
            res.append(nums2[ptr2])
            ptr2 += 1

        for i in range(len(nums1)):
            nums1[i]=res[i]
