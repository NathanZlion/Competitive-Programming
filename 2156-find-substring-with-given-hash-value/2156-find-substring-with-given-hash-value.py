class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        powers = [1]
        for _ in range(k):
            powers.append(powers[-1] * power)

        offset = ord('a')
        char_values = { char: ord(char) - offset + 1 for char in ascii_lowercase}

        runningHash = 0
        for i in range(k):
            runningHash +=  (char_values[s[i]]) * (powers[i])

        if runningHash % modulo == hashValue:
            return s[: k]
        
        for idx in range(k, len(s)):
            runningHash +=  (char_values[s[idx]]) * (powers[k])
            runningHash -= char_values[s[idx - k]]
            runningHash //= power
            
            if runningHash % modulo == hashValue:
                return s[idx - k + 1 : idx + 1]
