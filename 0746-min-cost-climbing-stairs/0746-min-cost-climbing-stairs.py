class Solution:
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        numOfStairs = len(cost)
        
        # iterative solution
        for index in range(2, numOfStairs):
            cost[index] += min(cost[index-1], cost[index-2])

        return min(cost[-1], cost[-2])

