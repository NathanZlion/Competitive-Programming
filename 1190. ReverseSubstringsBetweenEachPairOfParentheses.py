class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        openingTagStack = [] #last in first out

        index = 0
        while index < len(s): 
            if s[index] == "(":
                openingTagStack.append(index)
            elif s[index] == ")":
                if len(openingTagStack) > 0:
                    start = openingTagStack.pop()
                    s = s[:start] + s[index-1: start: -1] + s[index+1:]
                    index -=2
            index += 1

        return s
