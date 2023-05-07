class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        freq = defaultdict(int)

        for word in words:
            freq[word] += 1
        
        words = list(set(words))
        words.sort(key=lambda w: (-freq[w], w))

        return words[:k]

