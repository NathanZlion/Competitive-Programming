class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        modulus = 10**9 + 7
        count = defaultdict(int)
        res = 0
        
        for num in nums:
            target = num - int(str(num)[::-1])
            res += count[target]
            res %= modulus
            count[target] += 1
        
        return res