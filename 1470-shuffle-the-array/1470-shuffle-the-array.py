class Solution(object):
    def shuffle(self, nums, n):
        res = [0 for _ in range(2*n)]
        for i in range(n):
            res[2*i] = nums[i]
            res[2*i+1] = nums[i+n]
        
        return res
        