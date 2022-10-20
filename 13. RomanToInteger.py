class Solution:
    def romanToInt(self, s: str) -> int:
        # hash table of roman integers to integers
        dp = {'I':1,'V':5,'X':10,'L': 50,'C':100,'D':500,'M':1000,}
        if len(s)==1:return dp[s]
        prev = acc = dp[s[-1]]
        index, res = len(s)-2, 0
        while index>=0:
            currNumber = dp[s[index]]
            if currNumber >= prev:
                res += acc
                acc = currNumber
            else: acc -= currNumber
            if index == 0: res += acc
            prev = currNumber
            index -=1

        return res
