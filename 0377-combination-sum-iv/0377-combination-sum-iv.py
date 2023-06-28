class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        nums.sort()
        memo = {}

        def combination(currNum: int, currTarget: int) -> int:
            if currTarget == 0:
                return 1

            if ((currNum, currTarget) in memo):
                return memo[(currNum, currTarget)]

            sumOfCombinations = 0
            index = 0

            while index < len(nums) and nums[index] <= currTarget:
                nextNum = nums[index]
                sumOfCombinations += combination(nextNum, currTarget - nextNum)
                index += 1

            memo[(currNum, currTarget)] = sumOfCombinations

            return memo[(currNum, currTarget)]


        return combination(0, target)
