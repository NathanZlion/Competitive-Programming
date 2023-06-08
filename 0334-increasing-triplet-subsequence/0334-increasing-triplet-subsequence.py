class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        first = float('inf')
        second = float('inf')
        
        for num in nums:
            if num <= first:
                first = num
            
            elif num <= second:
                second = num

            # the number is greater both first and second we found our solution
            else:
                return True
        
        return False