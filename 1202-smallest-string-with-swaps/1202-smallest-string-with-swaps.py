class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # Union the indices by the pairs given
        # What we want to do is at each index pop the minimum alphabet from the
        # parent's family.

        self.reps = {i:i for i in range(len(s))}

        for idx1, idx2 in pairs:
            # union idx1 and idx2
            self.union(idx1, idx2)

        family = defaultdict(list)
        for index in range(len(s)):
            parent = self.find(index)
            heappush(family[parent], s[index])

        res = []
        for index in range(len(s)):
            parent = self.find(index)
            res.append(heappop(family[parent]))

        return "".join(res)


    def union(self, num1, num2):
        newRep = self.find(num2)
        
        while self.reps[num1] != num1:
            nxt = self.reps[num1]
            self.reps[num1] = newRep
            num1 = nxt

        self.reps[num1] = newRep


    def find(self, num):
        while self.reps[num] != num:
            num = self.reps[num]
        
        return num

