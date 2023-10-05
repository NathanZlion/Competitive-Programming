from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = Counter(nums)
        
        res = []
        for num, freqOfNum in freq.items():
            if freqOfNum > n//3:
                res.append(num)
        
        return res