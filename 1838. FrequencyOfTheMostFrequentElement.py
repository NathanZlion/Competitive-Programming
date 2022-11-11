class Solution(object):
    def maxFrequency(self, nums, k):
        nums.sort()
        res=1
        if len(nums)==1:return 1
        if len(nums)==2:
            if abs(nums[0] - nums[1]) <=k:return 2
            return 1
        right = len(nums)-1
        left=right-1
        while right >= left and right>-1:
            if left<0:
                return max(res,right+1)
            elif (nums[right]-nums[left]) <= k:
                k-=(nums[right] - nums[left])
                left-=1
            else:
                res = max(res, (right-left))
                k +=((right-left-1)*(nums[right] - nums[right-1]))
                right-=1
            
        return res
