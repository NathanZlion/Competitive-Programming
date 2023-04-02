class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        numsSet = set()

        for num in nums:
            freq[num] += 1
            numsSet.add(num)
        
        
        res = []
        for num in numsSet:
            res.append(num)

        res.sort(key = lambda x: freq[x])

        return res[len(res)-k:]

        