class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        length = [1]*n
        count = [1]*n
        
        for right in range(n):
            for left in range(right):
                # found smaller number to the left
                if nums[right] > nums[left]:
                    if length[right] < length[left]+1:
                        length[right] = length[left] + 1
                        count[right] = 0

                    if length[left] + 1 == length[right]:
                        count[right] += count[left]

        max_length = max(length)
        res = 0

        for index in range(n):
            if length[index] == max_length:
                res += count[index]

        return res
