class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        combinations = []

        def backTrack(index, path):

            if index > n+1:
                return

            if n - index + 1 + len(path) < k :
                return
            
            if len(path) == k:
                combinations.append(path[:])
                return

            nextPath = path[:]
            nextPath.append(index)
            backTrack(index+1, nextPath)
            backTrack(index+1, path)        

        backTrack(1, [])

        return combinations
