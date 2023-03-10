class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.possible_permutations = []

        def backTrace(built, available):

            if not available:
                self.possible_permutations.append([i for i in built])
                return

            for i in range(len(available)):
                built.append(available[i])
                backTrace(built, available[:i]+available[i+1:])
                built.pop()


        backTrace([], nums)

        return self.possible_permutations
