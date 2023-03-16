class Solution:
    def splitString(self, s: str) -> bool:
                
        self.possible = False

        def backTrack(left, right):

            leftInt = int(left)
            rightInt = int(right)


            if rightInt+1 == leftInt:
                self.possible  = True
                return True

            if rightInt < leftInt:
                return False

            for i in range(1,len(right)):
                if leftInt == int(right[:i]) + 1:
                    if backTrack(right[:i], right[i:]):
                        return True

            return False

        for i in range(1,len(s)):
            backTrack(s[:i], s[i:])

        return self.possible
