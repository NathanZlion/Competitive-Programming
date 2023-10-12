class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        count = 0
        freq = defaultdict(int)
        N = len(s)
        
        for right in range(N):
            freq[s[right]] += 1

            # we have made a viable window
            while freq['a'] and freq['b'] and freq['c']:
                count += (N - right)
                freq[s[left]] -= 1
                left += 1

        return count