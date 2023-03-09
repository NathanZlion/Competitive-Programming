class Solution:
    def splitString(self, s: str) -> bool:
        
        arr = [char for char in s]        
        
        self.possible = False

        def integ(arr):
            return int("".join(arr))

        def backTrack(left, right):
            print(left, right)

            leftInt = integ(left)
            rightInt = integ(right)

            if integ(right)+1  == leftInt:
                self.possible  = True
                return

            for i in range(1,len(right)):
                if leftInt == integ(right[:i]) + 1:
                    backTrack(right[:i], right[i:])


        for i in range(1,len(s)):
            backTrack(arr[:i], arr[i:])

        return self.possible
        
