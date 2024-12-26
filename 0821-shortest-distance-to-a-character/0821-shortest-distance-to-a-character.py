class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        indexOfChar = [index for index in range(len(s)) if s[index] == c]
        if len(indexOfChar) == 1:
            indexOfChar.append(indexOfChar[-1])
            
        ans = []
        leftPtr, rightPtr = 0, 1

        for index in range(len(s)):
            if rightPtr < (len(indexOfChar) - 1) and index > indexOfChar[rightPtr]:
                leftPtr += 1
                rightPtr += 1
            
            # try and find the minimum distance between the two es
            ans.append(
                min(
                    abs(index - indexOfChar[leftPtr]),
                    abs(index - indexOfChar[rightPtr])
                )
            )
        
        return ans
