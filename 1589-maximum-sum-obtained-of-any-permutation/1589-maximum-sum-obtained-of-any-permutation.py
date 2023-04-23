class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        counter = [0 for _ in range(len(nums)+1)]

        for start, end in requests:
            counter[start] += 1
            counter[end+1] -= 1

        # calculating the prefixsum
        for index in range(1, len(counter)):
            counter[index] += counter[index-1]

        nums.sort()
        counter.sort()
        maxSum = 0

        while counter:
            count = counter.pop()
            if count == 0:
                break
            maxSum += nums.pop() * count


        return maxSum % (10**9 + 7)

        