class Solution:

    def findCorrespondingRight(self, interval: List[int], index: int) -> int:
        low = index-1
        high = self.length

        while high > low+1:
            mid = low + (high-low)//2

            if self.intervals[mid][0] < interval[1]:
                low = mid
            else:
                high = mid

        return -1 if high == self.length else self.intervals[high][2]


    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        self.length = len(intervals)

        # appended the index for later access
        for index, interval in enumerate(intervals):
            interval.append(index)

        self.intervals = [i for i in sorted(intervals, key= lambda x:x[0])]
        res = [-1 for _ in range(self.length)]

        for index, interval in enumerate(self.intervals):
            res[interval[2]] = self.findCorrespondingRight(interval, index)

        return res

