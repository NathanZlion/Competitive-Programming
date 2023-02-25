class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.append(0)        
        for index in range(n):
            nums[index] = (nums[index-1] + nums[index]%2)

        nums.pop()

        # frequency of prefix sum before
        oddsMap = defaultdict(int)
        oddsMap[0] = 1
        
        count = 0
        for prefixSum in nums:
            count += oddsMap[prefixSum - k]
            oddsMap[prefixSum] += 1

        return count
            
        
        
            