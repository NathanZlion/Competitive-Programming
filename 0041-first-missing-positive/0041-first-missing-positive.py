class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        hash = {}

        for num in nums:
            if num > 0:
                hash[num] = 1
        
        i = 1
        
        while True:
            if not i in hash:
                return i
            i += 1
            
                