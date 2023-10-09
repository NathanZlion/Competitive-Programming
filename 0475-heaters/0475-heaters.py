class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def closestHeaterDistance(houseLocation: int) -> int:
            """
            finds 2 towers that are immediately to the left and right of it
            and return the minimum distance from the 2 and between the house
            """
            left = -1
            right = len(heaters)
            
            while right > left + 1:
                mid = (left + right) // 2
                
                # heater is to the left of the target house
                if houseLocation > heaters[mid]:
                    left = mid
                else:
                    right = mid

            left = max(left, 0)
            right = min(right, len(heaters)-1)

            return min(abs(heaters[left] - houseLocation), abs(heaters[right] - houseLocation))                

        houses.sort()
        heaters.sort()
        minR = 0
        for house in houses:
            minR = max(minR, closestHeaterDistance(house))
        
        return minR