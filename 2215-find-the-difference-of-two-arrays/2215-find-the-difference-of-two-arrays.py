class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        visited = set()

        res = [[], []]
        for num in nums1:
            if num not in nums2_set and num not in visited:
                res[0].append(num)
            
            visited.add(num)
        
        for num in nums2:
            if num not in nums1_set and num not in visited:
                res[1].append(num)

            visited.add(num)
        
        return res
