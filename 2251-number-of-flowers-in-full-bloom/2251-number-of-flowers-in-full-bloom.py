class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        prefixSum = defaultdict(int)

        for start, end in flowers:
            prefixSum[start] += 1
            prefixSum[end+1] -= 1
        
        keyInTime = list(sorted(prefixSum.keys()))
        count = [prefixSum[key] for key in keyInTime]
        
        for i in range(1, len(count)):
            count[i] += count[i-1]

        res = []
        for time in people:
            index = bisect_right(keyInTime, time)
            if index > len(keyInTime) or index == 0:
                res.append(0)
            else:
                res.append(count[index-1])

        return res