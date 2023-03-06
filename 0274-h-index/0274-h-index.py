class Solution:
    
    def hIndex(self, citations: List[int]) -> int:
        postfixsum = [0 for _ in range(1001)]

        for citation in citations:
            postfixsum[citation] += 1

        for i in range(999,-1,-1):
            postfixsum[i] += postfixsum[i+1]

        h_index = 0
        for index in range(1,1000):
            if postfixsum[index] >= index:
                h_index = index

        return h_index
