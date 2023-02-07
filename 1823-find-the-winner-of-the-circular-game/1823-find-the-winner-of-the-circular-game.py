class Solution(object):

    def findTheWinner(self, n, k):

        arr = [num+1 for num in range(n)]
        
        index = 0
        
        for _ in range(n-1):
            lnth = len(arr)
            index += k-1
            index %= lnth
            arr.pop(index)
            index %= lnth
            
        
        return arr[0]   