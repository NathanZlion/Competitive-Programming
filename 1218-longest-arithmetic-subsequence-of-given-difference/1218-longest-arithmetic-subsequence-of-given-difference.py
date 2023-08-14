from collections import defaultdict

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        memo = defaultdict(int)
    
        for index in range(len(arr)-1, -1, -1):
            memo[arr[index]] = memo[arr[index]+difference] + 1

        return max(memo.values())