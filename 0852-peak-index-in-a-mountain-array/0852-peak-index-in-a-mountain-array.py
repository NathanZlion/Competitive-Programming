class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # left = increasing
        # right = decreasing
        # finally find the place where the mountain peek
        left = 0
        right = len(arr) - 1
        
        
        while right > left + 1:
            mid = left + ((right-left)//2)
            
            # increasing
            if arr[mid] > arr[mid-1]:
                left = mid
            else:
                right = mid
        
        return left
