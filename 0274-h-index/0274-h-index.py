class Solution:
    
    def hIndex(self, citations: List[int]) -> int:
        count = [0 for _ in range(1001)]

        for citation in citations:
            count[citation] += 1

        postfixsum = [i for i in count]

        for i in range(999,-1,-1):
            postfixsum[i] += postfixsum[i+1]

        h_index = 0
        for mid in range(1,1000):
            if postfixsum[mid] >= mid:
                h_index = mid

        return h_index
