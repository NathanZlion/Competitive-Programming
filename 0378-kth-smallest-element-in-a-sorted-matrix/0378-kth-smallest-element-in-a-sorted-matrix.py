class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # kth smallest
        # n X n matrix
        # negate the numbers
        # heappop the numbers if greater than k
        # return the last element negated
        
        heap = []
        
        for nums in matrix:
            for num in nums:
                heappush(heap, num*-1)
        
        while len(heap) > k:
            heappop(heap)


        return heap[0] * -1
                            
        