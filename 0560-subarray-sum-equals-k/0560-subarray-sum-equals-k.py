class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        count = 0
        
        prefixMap = defaultdict(int)
        prefixMap[0]=1
        nums.append(0)
        
        for index in range(n):
            nums[index]+=nums[index-1]
            count += prefixMap[nums[index] - k]
            prefixMap[nums[index]] += 1

        return count
            
            
        
        