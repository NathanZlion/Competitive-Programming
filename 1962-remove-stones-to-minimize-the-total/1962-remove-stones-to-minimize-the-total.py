class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:

        for index in range(len(piles)):
            piles[index] *= -1

        heapify(piles)
        
        for _ in range(k):
            num = heappop(piles) * -1
            num -= num//2
            heappush(piles, num * -1)

        return sum(piles) * -1
