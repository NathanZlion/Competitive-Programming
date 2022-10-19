class Solution: 
    def select(self, arr, i):
        min_i = i
        for n in range(i, len(arr)):
            if arr[n] < arr[min_i]:
                min_i = n
        return min_i
    
    def selectionSort(self, arr,n):
        for i in range(len(arr)-1):
            min_index = self.select(arr, i)
            arr[i] , arr[min_index] = arr[min_index] , arr[i]
