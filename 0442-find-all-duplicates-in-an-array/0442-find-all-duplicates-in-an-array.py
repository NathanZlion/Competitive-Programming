class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = [0 for _ in range(100_000)]
        
        for num in nums:
            count[num] += 1
        
        res = []
        for i in range(max(nums)+1):
            if count[i] > 1:
                res.append(i)

        return res
