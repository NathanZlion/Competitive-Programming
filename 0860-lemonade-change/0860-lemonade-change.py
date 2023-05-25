class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        numberOfFives, numberOfTens = 0, 0

        for bill in bills:
            if bill == 5:
                numberOfFives += 1
            
            elif bill == 10:
                # we need to return a 5
                if numberOfFives <= 0:
                    return False

                numberOfFives -= 1
                numberOfTens += 1
            
            else:
                if numberOfFives > 0 and numberOfTens > 0:
                    numberOfFives -= 1
                    numberOfTens -= 1
                
                elif numberOfFives >= 3:
                    numberOfFives -= 3

                else:
                    return False
                
        
        return True