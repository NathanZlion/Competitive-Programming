class Solution:
    def validPartition(self, nums: List[int]) -> bool:        
        dp = [False]*(len(nums) + 2)
        dp[len(nums)] = True

        for index in range(len(nums)-2, -1,-1):
            dp[index] = (
                (dp[index+2] and (nums[index] == nums[index+1])) or
                (dp[index+3] and (nums[index] == nums[index+1] == nums[index+2])) or
                (dp[index+3] and \
                    (nums[index]+1 == nums[index+1]) and \
                    (nums[index+1]+1 == nums[index+2])
                )
            )

        return dp[0]