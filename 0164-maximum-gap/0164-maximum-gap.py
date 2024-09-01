import math

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        _min, _max = min(nums), max(nums)
        _range = _max - _min

        if _range == 0:
            return 0

        _length = len(nums)

        # make range to the nearest power of 10
        _power = round(math.log10(_range))
        # rangeInNearestPowerOfTen = 10 ** round(math.log10(_range))
        numOfBuckets = 10 ** (_power // 2)
        print(_range, numOfBuckets)
        # optimize : consider length of array in this

        buckets = [[] for _ in range(numOfBuckets)]
        for num in nums:
            bucketIndex = (numOfBuckets - 1) * (num - _min) // _range
            buckets[bucketIndex].append(num)

        sortedArr = []
        for bucket in buckets:
            bucket.sort()
            sortedArr.extend(bucket)
        
        leftPtr = 0
        maxContiguousGap = 0
        for rightPtr in range(len(sortedArr)):
            if sortedArr[rightPtr] == sortedArr[leftPtr]:
                continue

            diff = sortedArr[rightPtr] - sortedArr[leftPtr]
            maxContiguousGap = max(maxContiguousGap, diff)
            leftPtr = rightPtr

        return maxContiguousGap
