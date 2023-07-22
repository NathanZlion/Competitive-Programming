class Solution:
    def numTrees(self, n: int) -> int:        
        # memo = {}
        @cache
        def backtrack(left: int, right: int) -> int:
            # if (right-left) in memo: return memo[right-left]
            if right - left < 2:
                return 1

            possibilities = 0

            for node in range(left, right):
                left_subtree = backtrack(left=left, right=node)
                right_subtree = backtrack(left=node+1, right=right)
                curr_possibility = (left_subtree * right_subtree)
                possibilities += curr_possibility

            return possibilities

        return backtrack (left=0, right=n)
