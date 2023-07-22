class Solution:
    def numTrees(self, n: int) -> int:
        # number_of_nodes : number_of_possibilities
        memo = {0: 1, 1: 1}
        
        def backtrack(left: int, right: int) -> int:
            if (right-left) in memo:
                return memo[right-left]

            possibilities = 0

            for node in range(left, right):
                left_subtree = backtrack(left=left, right=node)
                right_subtree = backtrack(left=node+1, right=right)
                curr_possibility = (left_subtree * right_subtree)
                possibilities += curr_possibility

            memo[right-left] = possibilities

            return possibilities

        return backtrack (left=0, right=n)
