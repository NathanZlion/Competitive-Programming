class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        decodedLength = 0
        
        for char in s:
            if char.isdigit():
                decodedLength *= int(char)
            else:
                decodedLength += 1

        for i in range(len(s) - 1, -1, -1):
            char = s[i]

            if char.isdigit():
                currDigit = int(char)
                decodedLength //= currDigit
                k %= decodedLength

            else:
                # have we reached the answer
                if k == 0 or decodedLength == k:
                    return char

                decodedLength -= 1
