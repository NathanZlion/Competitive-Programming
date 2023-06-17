class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # my idea:
        # store in cache when returning up not to compute again
        # use a tuple (row, col) as a key and a minimum pathsum for it as a value
        # This should optimize the runtime to O(n) for the algorithm
        
        memo = {}
        
        def backTrack(row, col):
            # base case: reach leaf node
            if (row == len(triangle) - 1):
                memo[(row, col)] = triangle[row][col]

            # the memoization
            if ((row, col) in memo):
                return memo[(row, col)]

            # find minimum of the children and assign sum of it and my self to memo
            min_child = min(backTrack(row + 1, col), backTrack(row + 1, col + 1))
            memo[(row, col)] = min_child + triangle[row][col]

            return memo[(row, col)]


        return backTrack(0,0)