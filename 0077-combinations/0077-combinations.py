class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        combinations = []

        def backtrack(startIndex: int = 0, res: List[int] = []) -> None:
            # check if the length has been reached
            if len(res) == k:
                combinations.append(res.copy())

            for index in range(startIndex, n):
                res.append(index+1)
                backtrack(index+1, res)
                res.pop()

        backtrack()
        return combinations
