class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        for index in range(len(stones)):
            stones[index] *= -1
        
        heapify(stones)
        while len(stones) > 1:
            x = heappop(stones)
            y = heappop(stones)

            if x == y:
                continue
            else:
                heappush(stones, -1*(abs(x-y)))
        
        return -1*stones[0] if stones else 0