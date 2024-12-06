class Solution:
    def canChange(self, start: str, target: str) -> bool:
        startIndex = targetIndex = 0
        length = len(start)
        
        while startIndex < length or targetIndex < length:
            while startIndex < length and start[startIndex] == "_":
                 startIndex += 1

            while targetIndex < length and target[targetIndex] == "_":
                 targetIndex += 1
            
            # only one has ended
            if (startIndex == length) ^ (targetIndex == length):
                return False
            
            if (startIndex == length):
                break

            if start[startIndex] != target[targetIndex]:
                return False
                        
            if start[startIndex] == "L" and startIndex < targetIndex:
                return False
            
            if start[startIndex] == "R" and startIndex > targetIndex:
                return False
            
            startIndex += 1
            targetIndex += 1

        return startIndex == length ==targetIndex
