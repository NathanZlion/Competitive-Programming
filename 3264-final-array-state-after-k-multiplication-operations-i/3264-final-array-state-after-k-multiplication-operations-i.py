class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(num, index) for index, num in enumerate(nums)]
        heapify(heap)
        
        for _ in range(k):
            num, index = heappop(heap)
            nums[index] = num * multiplier
            heappush(heap, (num * multiplier, index))
        
        return nums
