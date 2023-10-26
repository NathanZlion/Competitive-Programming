class Solution:
    def compress(self, chars: List[str]) -> int:
        solution_arr = []
        stack = []
        
        for char in chars:
            if not stack:
                stack.append((char, 1))
            elif stack[-1][0] == char:
                _, prev_freq = stack.pop()
                stack.append((char, prev_freq + 1))
            else:
                prev_char, prev_freq = stack.pop()
                solution_arr.append(prev_char)
                if prev_freq > 1:
                    for num_char in str(prev_freq):
                        solution_arr.append(num_char)

                stack.append((char, 1))

        if stack:
            prev_char, prev_freq = stack.pop()
            solution_arr.append(prev_char)
            if prev_freq > 1:
                for num_char in str(prev_freq):
                    solution_arr.append(num_char)
        
        for index, char in enumerate(solution_arr):
            chars[index] = char
        
        return len(solution_arr)
            