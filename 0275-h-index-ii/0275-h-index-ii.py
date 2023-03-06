class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)-1

        low = 0
        high = n
        ans = 0

        while low <= high:
            mid = (low+high)//2

            if citations[mid] <= n-mid:
                low = mid + 1
            else:
                ans = max(ans, n-mid+1)
                high = mid - 1

        return ans
