class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:

        delta_x = abs(sx - fx)
        delta_y = abs(sy - fy)

        if delta_x == 0 and delta_y == 0 and t == 1:
            return False

        min_time = min(delta_x, delta_y) + abs(delta_x - delta_y)
        return min_time <= t