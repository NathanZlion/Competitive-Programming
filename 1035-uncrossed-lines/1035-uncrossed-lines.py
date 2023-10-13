class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        
        max_lines_crossed = 0

        @cache
        def traverse(ptr1: int, left_limit: int, lines_crossed: int) -> None:
            nonlocal max_lines_crossed

            if ptr1 == nums1_len:
                max_lines_crossed = max(max_lines_crossed, lines_crossed)
                return 
            
            for ptr2 in range(left_limit, nums2_len):
                if nums2[ptr2] == nums1[ptr1]:
                    traverse(ptr1 = ptr1 + 1, left_limit = ptr2 + 1, lines_crossed = lines_crossed + 1)
                    break
            
            traverse(ptr1 + 1, left_limit, lines_crossed)

        traverse(0, 0, 0)
        return max_lines_crossed
