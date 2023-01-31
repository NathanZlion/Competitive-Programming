class Solution: 
    def select(self, arr, i):
        min_ = i
        j = i+1
        n = len(arr)
        while j < n:
            if arr[min_] > arr[j]: min_ = j
            j += 1
        
        return min_
    
    def selectionSort(self, arr,n):
        for i in range(n-1):
            min_ = self.select(arr,i)
            arr[i], arr[min_] = arr[min_], arr[i]
            
