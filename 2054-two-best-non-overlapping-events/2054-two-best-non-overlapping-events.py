class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()

        def findNextNonOverlappingIndex(endTime: int, index: int) -> int:
            """
            returns the index of the first event that starts after the endTime,
            meaning that doesn't overlap with the event in consideration.
            """
            left = index
            right = len(events)
            
            while right > left + 1:
                mid = (left + right) // 2
                start, _, _ = events[mid]

                # overlaps
                if start <= endTime:
                    left = mid
                else:
                    right = mid
            
            return right

        @cache
        def dp(index: int, numSelected: int) -> int:
            """
            returns the maximum sum of non-overlapping [2 - numSelected] elements starting from index.
            """
            if numSelected == 2 or index == len(events):
                return 0

            # select current
            startTime, endTime, value = events[index]
            nextIndex = findNextNonOverlappingIndex(endTime, index)
            maxSum = dp(nextIndex, numSelected + 1) + value

            # skip current
            maxSum = max(maxSum, dp(index+1, numSelected))

            return maxSum

        return dp(0, 0)
