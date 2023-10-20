class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        for char in s:
            if char == '#':
                if stack1:
                    stack1.pop()
            else:
                stack1.append(char)
        
        stack2 = []
        for char in t:
            if char == '#':
                if stack2:
                    stack2.pop()
            else:
                stack2.append(char)

        if len(stack1) != len(stack2):
            return False
        
        for char1, char2 in zip(stack1, stack2):
            if char1 != char2:
                return False
            
        return True
                