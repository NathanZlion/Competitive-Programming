class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """ a → 0, e → 1, i → 2, o → 3, u → 4 """

        modulus = 1_000_000_007
        preceeded = {
            0: [1, 2, 4],
            1: [0, 2],
            2: [1, 3],
            3: [2],
            4: [2, 3]
        }

        dp = [[0 for _ in range(5)] for _ in range(n+1)]
        for i in range(5):
            dp[1][i] = 1

        for length in range(2, n+1):
            for vowel in range(5):
                for preceeder in preceeded[vowel]:
                    dp[length][vowel] += dp[length - 1][preceeder]
                    dp[length][vowel] %= modulus
        
        return sum(dp[n]) % modulus
