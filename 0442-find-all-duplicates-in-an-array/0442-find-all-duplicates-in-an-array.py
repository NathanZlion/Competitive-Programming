class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        max_ = max(nums) + 1
        count = [0 for _ in range(max_)]
        
        for num in nums:
            count[num] += 1
        
        res = []
        for i in range(max_):
            if count[i] > 1:
                res.append(i)

        return res
