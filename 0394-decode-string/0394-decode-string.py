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
            return s if not s.isdigit() else ""

        start, end = self.findBracketIndices(s)
        num_start_index = start-1

        while s[num_start_index].isdigit() and num_start_index > -1:
            num_start_index -= 1

        multiplier = int(s[num_start_index+1: start])

        return self.decodeString( s[:num_start_index + 1] + (multiplier* s[start+1:end]) + s[end+1:])
