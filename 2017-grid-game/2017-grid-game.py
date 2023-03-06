class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        prefix_sum = [i for i in grid[1]]
        postfix_sum = [i for i in grid[0]]

        prefix_sum.append(0)
        postfix_sum.append(0)

        for i in range(n):
            prefix_sum[i] += prefix_sum[i-1]

        for i in range(n-1,-1,-1):
            postfix_sum[i] += postfix_sum[i+1]


        # robot 1 optimal path
        min_ = float('inf')
        
        for index in range(n):
            min_ = min(min_, max(prefix_sum[index-1], postfix_sum[index+1]))

        return min_
        