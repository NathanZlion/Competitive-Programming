class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opening = '([{'
        closer = {
            '(':')',
            '[':']',
            '{':'}',
        }
        stack = []
        for parentheses in s:
            if parentheses in opening:
                stack.append(parentheses)
            elif len(stack) >0:
                last = stack.pop()
                if closer[last] ==parentheses:
                    pass
                else:
                    return False
            else:
                return False
        if len(stack) == 0:
            return True
        return False

