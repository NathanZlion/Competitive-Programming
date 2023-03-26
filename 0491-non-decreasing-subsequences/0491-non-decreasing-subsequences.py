class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        subsequences = set()
        arr = []

        def backTrack(index):
            if index == len(nums):
                if len(arr) >= 2:
                    subsequences.add(tuple(arr))
                return

            if nums[index] >= arr[-1]:
                arr.append(nums[index])
                backTrack(index + 1)
                arr.pop()

            backTrack(index + 1)

        for i in range(len(nums)):
            arr.append(nums[i])
            backTrack(i+1)
            arr.pop()

        return subsequences
