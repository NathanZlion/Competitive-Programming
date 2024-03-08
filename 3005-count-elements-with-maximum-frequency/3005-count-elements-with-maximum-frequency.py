class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)  # we get the count for every element
        maxCount = max(count.values())
        res = 0

        for element in count:
            if count[element] == maxCount:
                res += maxCount
        
        return res