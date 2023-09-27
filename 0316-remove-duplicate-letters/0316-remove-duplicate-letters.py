class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        seen = set()
        mono_stack = []
        count = Counter(s)
        
        for char in s:
            if not mono_stack:
                mono_stack.append(char)
                seen.add(char)

            elif char in seen:
                pass

            else:
                while mono_stack and mono_stack[-1] >= char and count[mono_stack[-1]] > 0:
                    seen.remove(mono_stack.pop())

                mono_stack.append(char)
                seen.add(char)

            count[char] -= 1

        return "".join(mono_stack)
                
                    
                    
        
