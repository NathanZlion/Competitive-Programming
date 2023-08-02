class Solution:
    def compress(self, chars: List[str]) -> int:
        res = []

        curr_char = chars[0]
        count = 1

        for index in range(1, len(chars)):
            char = chars[index]

            if char == curr_char:
                count += 1

            else:
                res.append(curr_char)
                if count > 1:
                    for int_char in str(count):
                        res.append(int_char)
                
                curr_char = char
                count = 1

        res.append(curr_char)
        if count > 1:
            for int_char in str(count):
                res.append(int_char)
        
        for index, char in enumerate(res):
            chars[index] = char

        return len(res)