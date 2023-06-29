class Solution:
    def combinationSum3(self, combLength: int, targetSum: int) -> List[List[int]]:

        combinations = set()

        def backTrack(currSum: int, currNum: int, prevList: List[int]) -> None:
            # base cases
            if currSum > targetSum or len(prevList) > combLength:
                return

            if len(prevList) == combLength:
                if currSum == targetSum: combinations.add(tuple(prevList))
                return

            if currNum > 9:
                return

            prevList.append(currNum)
            backTrack(currSum + currNum, currNum + 1, prevList)
            prevList.pop()

            backTrack(currSum, currNum + 1, prevList)
        
        backTrack(0, 1, [])

        return list(map(list, combinations))
