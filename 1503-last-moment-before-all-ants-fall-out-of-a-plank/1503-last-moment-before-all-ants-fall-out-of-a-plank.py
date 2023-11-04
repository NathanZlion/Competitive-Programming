class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        max_time = 0
        for position in left:
            max_time = max(max_time, position)
        
        for position in right:
            max_time = max(max_time, n - position)

        return max_time
