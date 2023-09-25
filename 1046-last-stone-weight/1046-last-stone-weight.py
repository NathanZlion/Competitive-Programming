class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # invert the sign to make a max heap
        stones = [-stone for stone in stones]
        heapify(stones)

        while len(stones) > 1:
            stone1 = heappop(stones)
            stone2 = heappop(stones)

            if stone2 - stone1 > 0:
                heappush(stones, stone1 - stone2)

        return -stones[0] if stones else 0
