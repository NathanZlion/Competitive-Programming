class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                dp[r][c] = max (
                    dp[r+1][c],
                    dp[r][c+1],
                )

                if nums1[c] == nums2[r]:
                    dp[r][c] = max(dp[r][c], 1 + dp[r+1][c+1])


        return dp[0][0]