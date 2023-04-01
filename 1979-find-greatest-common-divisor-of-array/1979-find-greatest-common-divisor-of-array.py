class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a

        if a == 0:
            return b

        return self.gcd(min(a,b), max(a,b)%min(a,b))

    def findGCD(self, nums: List[int]) -> int:
        return self.gcd(max(nums), min(nums))