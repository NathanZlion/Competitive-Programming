class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        freq = defaultdict(int)

        for num in nums:
            freq[num] +=1

            if freq[num] > n//2:
                return num