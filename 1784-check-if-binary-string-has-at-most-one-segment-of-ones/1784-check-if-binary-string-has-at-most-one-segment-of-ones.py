class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        """
        Maybe count the ones, then run a fixed window slide then count if you can reach the number of 
        """

        countOfOnes = Counter(s)["1"]
        left = 0
        runningOnesCount = 0
        
        for right in range(len(s)):
            if s[right] == "1":
                runningOnesCount += 1
            
            # move window left bound if size is big
            if (right - left + 1) > countOfOnes:
                runningOnesCount -= s[left] == "1"
                left += 1
            
            if runningOnesCount == countOfOnes:
                return True
        
        return False
