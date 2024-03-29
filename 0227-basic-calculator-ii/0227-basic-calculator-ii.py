class Solution:
    def calculate(self, s: str) -> int:
        s = "".join(s.split()) # getting rid of the empty spaces

        splitted_expression = []
        op_func = {
            '+': operator.__add__,
            '-': operator.__sub__,
            '*': operator.__mul__,
            '/': operator.__floordiv__
        }

        running_num = 0
        for char in s:
            if char in op_func:
                splitted_expression.append(running_num)
                splitted_expression.append(char)
                running_num = 0
            else:
                running_num = (running_num * 10) + int(char)

        splitted_expression.append(running_num)

        def operate(operators, expression):
            stack = []
            i = 0
            while i < len(expression):
                curr_char = expression[i]

                if isinstance(curr_char, int) or curr_char not in operators:
                    stack.append(curr_char)
                else:
                    stack.append(op_func[curr_char](stack.pop(), expression[i+1]))
                    i += 1

                i += 1

            return stack

        # first do mul and div then do add and sub operations
        return operate(['-', '+'], operate(['*','/'], splitted_expression)).pop()
