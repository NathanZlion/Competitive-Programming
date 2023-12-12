class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = nums.copy()
        for i in range(1, len(running_sum)):
            running_sum[i] += running_sum[i - 1]

        return running_sum
