class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        def backTrack(lst: List[int], index:int):
            if sum(lst) > target:
                return 

            if sum(lst) == target:
                combinations.append(lst.copy())
                return 

            for idx in range(index, len(candidates)):
                lst.append(candidates[idx])
                backTrack(lst, idx)
                lst.pop()


        backTrack([], 0)


        return combinations