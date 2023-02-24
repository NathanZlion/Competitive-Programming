class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = 0
        for log in logs:
            if log == "../":
                if stack: stack -= 1
            elif log == './':
                pass
            else:
                stack += 1
        
        return stack
        