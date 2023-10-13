class Solution:
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        numOfStairs = len(cost)
        for i in range(2, numOfStairs):
            cost[i] += (min(cost[i-1], cost[i-2]))

        return cost[-1]