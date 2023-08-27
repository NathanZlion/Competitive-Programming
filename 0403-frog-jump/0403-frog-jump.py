class Solution:
    def canCross(self, stones: List[int]) -> bool:

        def searchToRight(start, target):
            left = start # < target
            right = len(stones) # >= the target
            
            while right > left + 1:
                mid = (left + right)//2
                if stones[mid] >= target:
                    right = mid
                else:
                    left = mid

            return right

        @cache
        def backtrack(index, prevStep):
            if index == len(stones) - 1:
                return True

            for step in set([-1, 0, 1]):
                target = stones[index] + prevStep + step
                nextIndex = searchToRight(
                    start = index,
                    target = target
                )

                if nextIndex < len(stones) and stones[nextIndex] == target:
                    if backtrack(nextIndex, prevStep + step):
                        return True

            return False

        if stones[0] != 0 or stones[1] != 1:
            return False

        return backtrack(1, 1)