class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        def mapToChar(num: int) -> str:
            return chr(num+65)

        numArr = []
        while columnNumber > 0:
            columnNumber -= 1
            numArr.append(columnNumber%26)
            columnNumber //= 26
        
        numArr.reverse()
        return ''.join([mapToChar(num) for num in numArr])
