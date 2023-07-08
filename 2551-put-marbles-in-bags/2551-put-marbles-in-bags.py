class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        max_heap = []
        min_heap = []

        for index in range(n - 1):
            cost = weights[index] + weights[index + 1]
            max_heap.append(cost)
            min_heap.append(-cost)
        
        heapq.heapify(max_heap)
        heapq.heapify(min_heap)
        
        answer = 0
        for index in range(k - 1):
            answer -= heapq.heappop(max_heap) + heapq.heappop(min_heap)

        return answer