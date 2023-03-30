class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        self.permutations = []
        self.lst = []

        for char in s:
            self.lst.append(char)


        def backTrack(index):
            if index == len(self.lst):
                self.permutations.append("".join(self.lst))
                return
            
            if self.lst[index].isalpha():
                self.lst[index] = self.lst[index].lower()
                backTrack(index+1)
                self.lst[index] = self.lst[index].upper()
                backTrack(index+1)
            else:
                backTrack(index+1)

        backTrack(0)


        return self.permutations
        