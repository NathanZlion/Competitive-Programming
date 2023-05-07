class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        freq = defaultdict(int)

        for word in words:
            freq[word] += 1
        
        heap = []
        for word, count in freq.items():
            heap.append((count*-1, word))

        heapify(heap)
        
        res = []
        for _ in range(k):
            count, word = heappop(heap)
            res.append(word)

        return res
        
            
            