class Solution:
    
    def isValidMaximum(self, maxNum: int, arr: List[int]) -> bool:

        for index in range(len(arr)-1, 0,-1):            
            if arr[index] > maxNum:
                temp = arr[index]
                arr[index] = maxNum
                arr[index-1] += (temp - maxNum)

        return arr[0] <= maxNum


    def minimizeArrayValue(self, nums: List[int]) -> int:

        high = max(nums)
        low = -1

        while high > low+1:
            mid = low + (high - low)//2

            if self.isValidMaximum(mid, nums[:]):
                high = mid
            else:
                low = mid
        
        return high
