class Hash:
    MOD = 10**9+7
    a = 26
    def __init__(self, val: int = 0, count: int = 0):
        self.val = val
        self.count = count

    def addFirst(self, char: str):
        addCharInt = Hash.charToInt(char)
        self.val *= Hash.a
        self.val += addCharInt
        self.val %= Hash.MOD
        self.count += 1
    
    def pollLast(self, char: str) -> None:
        popCharInt = Hash.charToInt(char)
        self.val -= (popCharInt * Hash.a**(self.count-1))
        self.val %= Hash.MOD
        self.count -= 1

    @staticmethod
    def charToInt(char: str):
        return ord(char) - ord('a') + 1

    @staticmethod
    def hash(word: str) -> 'Hash':
        n = len(word)
        val = 0
        a = 26
        for i in range(n):
            val *= a
            val += Hash.charToInt(word[i])
            val %= Hash.MOD

        return Hash(val, n)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        k = len(needle)
        
        if k > n:
            return -1

        targetHashVal = Hash.hash(needle).val
        runningHash = Hash.hash(haystack[:k])

        if runningHash.val == targetHashVal and haystack[:k] == needle:
            return 0
        
        for i in range(1, n - k + 1):
            runningHash.addFirst(haystack[i + k - 1])
            runningHash.pollLast(haystack[i - 1])

            if runningHash.val == targetHashVal:
                if haystack[i:i + k] == needle:
                    return i
        
        return -1