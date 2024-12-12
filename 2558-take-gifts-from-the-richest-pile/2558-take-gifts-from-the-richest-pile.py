class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-gift for gift in gifts]
        
        heapify(heap)
        for _ in range(k):
            # choose the maximum
            maxGift = -heappop(heap)
            leaveBehind = floor(sqrt(maxGift))
            heappush(heap, -leaveBehind)
        
        return -sum(heap)
