class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        max_score = min_num = nums[k]
        ptr1 = ptr2 = k
        n = len(nums)

        while ptr1 > 0 or ptr2 < n-1:
            # if expanding window both ways is possible
            if ptr1 > 0 and ptr2 < n-1:
                if nums[ptr1 - 1] > nums[ptr2 + 1]:
                    ptr1 -= 1
                    min_num = min(min_num, nums[ptr1])
                else:
                    ptr2 += 1
                    min_num = min(min_num, nums[ptr2])

            # if expanding window left is possible
            elif ptr1 > 0:
                ptr1 -= 1
                min_num = min(min_num, nums[ptr1])

            # if expanding window right is possible
            else:
                ptr2 += 1
                min_num = min(min_num, nums[ptr2])

            max_score = max(max_score, min_num * (ptr2 - ptr1 + 1))

        return max_score
            