class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # store a memo dictionary of the maximum points you can earn at each index
        memo = {}
        
        def maxPoint(index : int) -> int:
            if index in memo:
                return memo[index]
            
            # baseCase
            if index >= len(questions):
                return 0
            
            # we have 2 choices, solve or skip
            currPoint, currBrainPower = questions[index]

            solvePoint = currPoint + maxPoint(index + currBrainPower + 1)
            skipPoint = maxPoint(index+1)

            memo[index] = max(solvePoint, skipPoint)

            return memo[index]

        return maxPoint(0)            
        