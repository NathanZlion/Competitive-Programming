class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)

        def toBinary(word: str) -> int:
            binary = 0
            for char in word:
                binary |= (1 << (ord('z') - ord(char)))

            return binary

        binaryRepr = { word: toBinary(word) for word in words }
        
        res = 0
        for i in range(n):
            for j in range(n):
                # no overlapping character
                if binaryRepr[words[i]] & binaryRepr[words[j]] == 0:
                    res = max(res, (len(words[i]) * len(words[j]) ))

        return res