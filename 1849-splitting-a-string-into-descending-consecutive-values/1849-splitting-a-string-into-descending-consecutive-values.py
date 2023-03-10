class Solution:
    def splitString(self, s: str) -> bool:
        
        arr = [char for char in s]        
        
        self.possible = False

        def integ(arr):
            return int("".join(arr))

        def backTrack(left, right):

            leftInt = integ(left)
            rightInt = integ(right)
            

            if integ(right)+1 == leftInt:
                self.possible  = True
                return True

            if rightInt < leftInt:
                return False

            for i in range(1,len(right)):
                if leftInt == integ(right[:i]) + 1:
                    if backTrack(right[:i], right[i:]):
                        return True
            return False

        for i in range(1,len(s)):
            backTrack(arr[:i], arr[i:])

        return self.possible
        
