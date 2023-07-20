class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        stairs_steps = [0]*n
        stairs_steps[0] = 1
        stairs_steps[1] = 2

        for step in range(2, n):
            stairs_steps[step] = stairs_steps[step-1] + stairs_steps[step-2]
        
        return stairs_steps[-1]