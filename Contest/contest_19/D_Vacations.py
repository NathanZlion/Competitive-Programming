import sys

n = sys.stdin.readline()
arr = list(map(int, sys.stdin.readline().split()))


class Solution:
    @staticmethod
    def solve(arr):
        logg = [(0, 0)]
        min_rests = len(arr)
        memo = {}

        def backtrack(prev, index, daysRested):
            nonlocal min_rests
            nonlocal logg

            if index == len(arr):
                min_rests = min(min_rests, daysRested)
                return

            if daysRested >= min_rests or (index, prev[0], prev[1]) in memo:
                return

            if arr[index] > 1:  # if gym is open
                if prev[0] == 0:  # haven't gone yesterday, go to gym
                    backtrack((1, 0), index + 1, daysRested)

            if arr[index] % 2:  # contest is carried out
                if prev[1] == 0:  # haven't written yesterday
                    backtrack((0, 1), index + 1, daysRested)

            backtrack((0, 0), index + 1, daysRested + 1) # chilling, no gym, no contest ...

            # Memoize the result
            memo[(index, prev[0], prev[1])] = min_rests

        backtrack((0, 0), 0, 0)
        return min_rests


print(Solution.solve(arr))
