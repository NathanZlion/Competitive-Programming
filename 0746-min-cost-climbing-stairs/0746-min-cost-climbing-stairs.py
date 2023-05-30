class Solution:
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {}

        def recursion(index):
            # base case
            if index == len(cost)-1 or index == len(cost)-2:
                return cost[index]
            
            if index in memo:
                return memo[index]

            res = cost[index] + min(recursion(index+1), recursion(index+2))
            memo[index] = res
            return res


        return min(recursion(0), recursion(1))
