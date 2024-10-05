class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:        

        # what we're looking for is a subarray whose sum 
        # has remainder this with respect to p
        subarrayReminderNeeded = sum(nums) % p
        
        if subarrayReminderNeeded == 0:
            return 0
        
        prefixRemainder = {0 : -1}
        runningReminder = 0
        shortestSubarrayLen = len(nums)
        
        for right in range(len(nums)):
            runningReminder += nums[right]
            runningReminder %= p
            
            reminderNeeded = (runningReminder - subarrayReminderNeeded) % p
            if reminderNeeded in prefixRemainder:
                subarrrayToRemoveLength = right - prefixRemainder[reminderNeeded]
                shortestSubarrayLen = min(shortestSubarrayLen, subarrrayToRemoveLength)
            
            prefixRemainder[runningReminder] = right
        
        return shortestSubarrayLen if shortestSubarrayLen < len(nums) else -1
