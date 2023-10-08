from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:        
        n, m = len(nums1), len(nums2)
        dp = [[0] * n for _ in range(m)]

        for i in range(n):
            for j in range(m):
                dp[j][i] = nums1[i] * nums2[j]

                if i > 0:
                    dp[j][i] = max(dp[j][i], dp[j][i-1])

                if j > 0:
                    dp[j][i] = max(dp[j][i], dp[j-1][i])

                if i > 0 and j > 0:
                    dp[j][i] = max(dp[j][i], dp[j-1][i-1] + nums1[i] * nums2[j])


        return dp[m-1][n-1]