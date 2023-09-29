class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        res = 0
        for i in range(n):
            char = columnTitle[i]
            power = n-i-1
            res += ((ord(char) - ord('A') + 1) * (26**power))
        
        return res