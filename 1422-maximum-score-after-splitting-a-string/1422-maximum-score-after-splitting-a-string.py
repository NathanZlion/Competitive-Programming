class Solution:
    def maxScore(self, s: str) -> int:
        max_score = count_zeros_left = 0
        count_ones_right = s.count('1')
        n = len(s)

        for i in range(n - 1):
            count_zeros_left += s[i] == '0'
            count_ones_right -= s[i] == '1'
            max_score = max(max_score, count_zeros_left + count_ones_right)

        return max_score