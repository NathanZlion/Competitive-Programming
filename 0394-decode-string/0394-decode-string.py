class Solution:
    def findBracketIndices(self, string: str) -> List[int]:
        stack = []
        for index, char in enumerate(string):
            if char == '[':
                stack.append(index)
            elif char == ']':
                return [stack.pop(), index]                

        
    def decodeString(self, s: str) -> str:
        if not '[' in s:
            return s if not s.isnumeric() else ""

        # find the most inner bracket to decode
        # stack the brackets until popped
        start, end = self.findBracketIndices(s)

        num_start_index = start-1

        while s[num_start_index].isnumeric() and num_start_index >= 0:
            num_start_index -= 1
        
        num_start_index += 1
        num = int(s[num_start_index: start])

        ans = s[:num_start_index] + (num* s[start+1:end]) + s[end+1:]
        
        return self.decodeString(ans)
        