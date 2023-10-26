class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr = 0
        n = len(s)

        for char in t:
            if ptr == n:
                return True

            if s[ptr] == char:
                ptr += 1

        return ptr == n
