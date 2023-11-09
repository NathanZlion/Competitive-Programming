class Solution:

    def arithmeticSum(self, n: int) -> int:
        return (n) * (n+1) // 2

    def countHomogenous(self, s: str) -> int:
        if not s:
            return 0
        
        n = len(s)
        modulus = 1_000_000_007
        left = 0
        num_homogenous_substrings = 0

        while left < n:
            right = left

            while right < n-1 and s[right + 1] == s[left]:
                right += 1

            substring_len = right - left + 1
            num_homogenous_substrings += self.arithmeticSum(substring_len)
            num_homogenous_substrings %= modulus
            left = right + 1

        return num_homogenous_substrings
