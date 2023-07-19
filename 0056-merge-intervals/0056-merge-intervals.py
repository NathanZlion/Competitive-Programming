class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort them initially
        # traverse the intervals

        intervals.sort()
        merged = []
        curr_start, curr_end = intervals[0]

        for (start, end) in intervals:
            if start > curr_end:
                merged.append([curr_start, curr_end])
                curr_start, curr_end = start, end
            else:
                # incorporate into current interval
                curr_end = max(curr_end, end)

        if not merged or curr_start > merged[-1][1]:
            merged.append([curr_start, curr_end])

        return merged
