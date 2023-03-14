class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def invert(arr):
            for index, num in enumerate(arr):
                arr[index] = 0 if num == 1 else 1
            
            return arr


        def backTrack(n, arr):
            if n == 1:
                return arr
            
            return backTrack(n-1, arr + [1] + invert(arr[::-1]))


        return str(backTrack(n, [0])[k-1])
