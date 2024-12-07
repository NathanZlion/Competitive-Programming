class Solution:
    def minNumOperations(self, nums: List[int], penalty: int) -> int:
        res = 0
        for num in nums:
            res += max(0, math.ceil(num / penalty) - 1)

        return res

    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        maxNum = max(nums)
        left = 0
        right = maxNum + 1
        
        while right > left + 1:
            mid = (left + right) // 2
            minOperations = self.minNumOperations(nums, mid)
            if minOperations > maxOperations:
                # not achievable
                left = mid
            else:
                right = mid
        
        return right
