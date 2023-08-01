class Solution:

    def isDivisor(self, substring: str, string: str) -> bool:

        if len(string) % len(substring):
            return False

        chunkLength = len(substring)
        numberOfChunks = len(string) // len(substring)
        for i in range(numberOfChunks):
            for j in range(chunkLength):
                idx = (i * chunkLength) + j
                if string[idx] != substring[j]:
                    return False

        return True


    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""

        for index in range(min(len(str1), len(str2))):
            if str1[index] != str2[index]:
                break

            substring = str1[:index+1]
            if self.isDivisor(substring, str1) and self.isDivisor(substring, str2):
                res = str1[:index+1]

        return res
