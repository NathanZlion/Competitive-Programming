class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        windows = [(num - k, num + k) for num in nums]
        windows.sort() # sort them by start time
        
        # min heap contains end times
        heap = []
        maximumOverlap = 0
        
        for start, end in windows:
            while heap and heap[0] < start:
                heappop(heap)

            heappush(heap, end)
            maximumOverlap = max(maximumOverlap, len(heap))

        return maximumOverlap
