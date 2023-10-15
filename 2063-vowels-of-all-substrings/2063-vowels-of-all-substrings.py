class Solution:
    def countVowels(self, word: str) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        res = 0
        N = len(word)

        for index, char in enumerate(word):
            if char in vowels:
                res += ((index+1) * (N-index))

        return res
