class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        low = 0
        high = n-1
        best = 0

        while low <= high:
            mid = (low+high)//2

            if n-mid <= citations[mid]:
                best = mid
                high = mid - 1
            else:
                low = mid + 1

        return n - best if citations[best] else 0
    
