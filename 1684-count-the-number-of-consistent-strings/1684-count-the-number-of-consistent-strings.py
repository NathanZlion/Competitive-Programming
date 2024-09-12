class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        consistentStringCount = 0
        for word in words:
            for char in word:
                if char not in allowed:
                    break
            else:
                consistentStringCount += 1

        return consistentStringCount
