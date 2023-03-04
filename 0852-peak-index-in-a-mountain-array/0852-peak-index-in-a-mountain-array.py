class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        arr.append(-1)
        
        n = len(arr)
        low = -1
        high = n
        
        while high > low+1:
            mid = (high + low)//2
            if arr[mid] > arr[mid-1]:
                low = mid
            else:
                high = mid
        
        return low