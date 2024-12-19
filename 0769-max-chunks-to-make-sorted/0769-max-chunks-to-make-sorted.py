class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sortedArr = sorted(arr)
        set1 = set()
        set2 = set()
        
        matchingSubsets = 0
        for index in range(len(arr)):
            set1.add(arr[index])
            set2.add(sortedArr[index])
            
            if set1 == set2:
                matchingSubsets += 1
        
        return matchingSubsets            
