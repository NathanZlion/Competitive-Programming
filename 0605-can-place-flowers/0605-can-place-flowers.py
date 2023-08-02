class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        planted = 0

        def canPlantHere(index: int) -> bool:
            # check left side
            if index > 0 and flowerbed[index-1] == 1:
                return False
            
            # check right side
            if index < len(flowerbed)-1 and flowerbed[index+1] == 1:
                return False
            
            return True
        
        for index, plot in enumerate(flowerbed):
            if plot == 0:
                if canPlantHere(index):
                    flowerbed[index] = 1
                    planted += 1


        return planted >= n
