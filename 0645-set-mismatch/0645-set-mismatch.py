class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        n = len(nums)
        count = [0 for _ in range(n)]
        
        res = [0,0]

        for num in nums:
            if count[num-1] == 1:
                res[0] = num
            count[num-1] = 1

        for index in range(n):
            if count[index] == 0:
                res[1] = index+1
                break
        
        return res
                
            
        