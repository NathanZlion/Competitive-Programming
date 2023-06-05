class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        
        # sort the array
        # starting from the left
        # make the first element 1 || Then moving right reduce the numbers until their 
        # difference become lessthat 2
        
        arr.sort()
        arr[0] = 1
        
        for index in range(1, len(arr)):
            if arr[index] > arr[index-1] + 1:
                arr[index] = arr[index-1] + 1
            
        
        return arr[-1]
            
        