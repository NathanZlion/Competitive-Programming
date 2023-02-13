class Solution(object):
    def countOdds(self, low, high):
        if low == high:
            if low%2: return 1
            return 0
        
        if low%2 or high%2:
            return (high-low)//2+1
        return (high-low)//2