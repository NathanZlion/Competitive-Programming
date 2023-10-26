class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr).values()

        return len(set(freq)) == len(freq)