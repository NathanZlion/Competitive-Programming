class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        memo = defaultdict(int)

        for index in range(len(arr)):
            memo[arr[index]] = 1 + memo[arr[index] - difference]
        
        memo[10001] = 1

        return max(memo.values())