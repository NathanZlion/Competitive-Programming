class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        def backTrack(sum_: int, lst: List[int], index:int):
            if sum_ > target:
                return 

            if sum(lst) == target:
                combinations.append(lst.copy())
                return 

            for idx in range(index, len(candidates)):
                lst.append(candidates[idx])
                backTrack(sum_ + candidates[idx],lst, idx)
                lst.pop()
                


        backTrack(0, [], 0)


        return combinations