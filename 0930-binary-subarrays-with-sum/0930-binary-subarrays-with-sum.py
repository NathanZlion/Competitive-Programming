class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        count = 0
        freq = defaultdict(int)
        freq[0] = 1
        
        
        runningSum = [num for num in nums]
        runningSum.append(0)
        
        for i in range(len(nums)):
            runningSum[i] += runningSum[i-1]
        
        
        for index in range(len(nums)):
            num = runningSum[index]
            count += freq[num - goal]
            freq[num] += 1

        return count

        