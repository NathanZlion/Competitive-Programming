class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if not stack:
                stack.append([char, 1])
                continue
            
            if stack[-1][0] == char:
                stack[-1][1] += 1
                while stack and stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])

        res = [char*count for char, count in stack]
        return ''.join(res)