class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        curr = 0
        stack = []
        for parenthesis in s:
            if parenthesis == '(':
                stack.append(0)
            
            else:
                multiplier = stack.pop()
                curr = 1 if multiplier == 0 else multiplier*2
            
                if stack:
                    stack[-1] += curr
                else:
                    score += curr
                
        return score
