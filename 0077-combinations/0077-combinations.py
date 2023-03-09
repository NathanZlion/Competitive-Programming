class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        combinations = []

        def backTrack(index, path):
            
            if index > n+1:
                return
            
            if len(path) == k:
                combinations.append(path[:])
                return
            
            list1 = path[:]
            list1.append(index)
            backTrack(index+1, list1)
            
            backTrack(index+1, path)        

        backTrack(1, [])

        return combinations
