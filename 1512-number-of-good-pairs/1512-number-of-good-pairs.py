class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        goodPairsCount = 0
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
            goodPairsCount += (count[num]-1)

        return goodPairsCount