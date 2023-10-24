class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbedLen = len(flowerbed)
        
        for index, val in enumerate(flowerbed):
            if index > 0 and flowerbed[index-1] == 1:
                continue

            if index < flowerbedLen - 1 and flowerbed[index+1] == 1:
                continue
            
            n -= (1 - flowerbed[index])
            flowerbed[index] = 1 

        return n <= 0
