class Solution(object):
    def shuffle(self, nums, n):
        arr1 = nums[:n]
        arr2 = nums[n:]
        res = []
        for i in range(n):
            res.append(arr1.pop(0))
            res.append(arr2.pop(0))
        
        return res
        