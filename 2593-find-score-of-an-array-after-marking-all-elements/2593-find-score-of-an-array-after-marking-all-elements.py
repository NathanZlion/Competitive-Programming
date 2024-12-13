class Solution:
    def findScore(self, nums: List[int]) -> int:
        sortedNums = [(nums[index], index) for index in range(len(nums))]
        sortedNums.sort()
        
        marked = set()
        score = 0
        
        for index in range(len(nums)):
            num, idx = sortedNums[index]
            if idx in marked:
                continue

            score += num
            marked.add(idx-1)
            marked.add(idx)
            marked.add(idx+1)
        
        return score
