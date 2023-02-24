class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        
        stack = []
        for brace in s:
            if brace in bracketMap:
                stack.append(brace)
            
            elif not(stack and bracketMap[stack.pop()] == brace):
                return False

        return not stack
