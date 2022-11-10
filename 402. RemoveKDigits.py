class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k-=1
            stack.append(digit)
        while k>0:
            stack.pop()
            k-=1
        if not stack: return "0"
        res="".join(stack)
        
        # used casting to get rid of leading zeros.
        return str(int(res))
