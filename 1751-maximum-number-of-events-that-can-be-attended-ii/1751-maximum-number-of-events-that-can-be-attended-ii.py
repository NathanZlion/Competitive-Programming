from functools import cache
from typing import List

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events = sorted(events, key=lambda x: (x[0], x[1]))

        @cache
        def nextPossibleIndex(startIndex: int, date: int) -> int:
            left = startIndex
            right = len(events)

            while right > left + 1:
                mid = (left + right) // 2

                if events[mid][0] > date:
                    right = mid
                else:
                    left = mid

            return right

        @cache
        def maxVal(index: int, remainingUnattended: int) -> int:
            if index >= len(events) or remainingUnattended == 0:
                return 0

            startDate, endDate, currVal = events[index]

            # Ignore the current event
            dontAttendValue = maxVal(index + 1, remainingUnattended)

            # Attend the current event
            nextIndex = nextPossibleIndex(index, endDate)
            attendValue = currVal

            if nextIndex < len(events):
                attendValue += maxVal(nextIndex, remainingUnattended - 1)

            return max(attendValue, dontAttendValue)

        return maxVal(index = 0, remainingUnattended = k)
