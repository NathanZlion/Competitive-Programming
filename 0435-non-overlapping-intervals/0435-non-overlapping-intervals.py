class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # sort the intervals to get a time line
        intervals.sort()

        memo = {}
        
        def next_nonoverlapping(start_index, end_date):
            left = start_index
            right = len(intervals)
            
            # right points to possible date

            while right > left + 1:
                mid = left + ((right - left) // 2)
                curr_start_date, _ = intervals[mid]
                
                if curr_start_date >= end_date:
                    right = mid
                
                else:
                    left = mid

            return right


        def traverse(index):
            if index in memo:
                return memo[index]
            
            if index >= len(intervals):
                return 0

            _, end = intervals[index]

            # consider the current interval
            add_curr = 1 + traverse(next_nonoverlapping( index, end))
            ignore_curr = traverse(index+1)

            memo[index] = max(add_curr, ignore_curr)

            return memo[index]            

        max_intervals = traverse(0)

        # to get the minimum number of intervals that have to be removed 
        # to attain a non-overlapping intervals subtract the maximum possible 
        # number of intervals non overlapping intervals

        return len(intervals) - max_intervals