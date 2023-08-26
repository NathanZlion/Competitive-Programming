class Solution:
    @staticmethod
    def binarySearch (target, start, arr):
        left = start
        right = len(arr)
        while right > left + 1:
            mid = (left + right)//2
            if arr[mid][0] > target:
                right = mid
            else:
                left = mid

        return right


    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        dp = [1]*(len(pairs)+1)

        for index in range(len(pairs)-1, -1, -1):
            nextChainIndex = Solution.binarySearch(pairs[index][1], index, pairs)
            dp[index] = dp[index+1]
            if nextChainIndex < len(pairs):
                dp[index] = max(1 + dp[nextChainIndex], dp[index])

        return dp[0]
