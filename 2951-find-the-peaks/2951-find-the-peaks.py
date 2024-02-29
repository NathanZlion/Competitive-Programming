class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        ans = []
        n = len(mountain)

        for index in range(n - 2):
            if mountain[index] < mountain[index + 1] > mountain[index + 2]:
                ans.append(index + 1)
        
        return ans
