class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        
        cur_num = 1
        n = len(arr)
        for index in range(n):
            cur_num = min(cur_num, arr[index])
            arr[index] = cur_num
            cur_num += 1
        
        return arr[n-1]