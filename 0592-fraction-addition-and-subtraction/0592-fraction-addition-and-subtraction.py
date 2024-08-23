class Solution:
    def fractionAddition(self, expression: str) -> str:
        operations = set(['-', '+'])
        
        def evaluate(expression1: str, expression2: str):
            num1, deno1 = expression1.split('/')
            num2, deno2 = expression2.split('/')

            num1, num2, deno1, deno2 = map(int, [num1, num2, deno1, deno2])
            
            resultNumerator = (deno2 * num1) + (deno1 * num2)
            resultDenominator = deno1 * deno2

            return f'{resultNumerator}/{resultDenominator}'


        def reduce(expression):
            num, deno = map(int, expression.split('/'))

            if num == 0:
                return f'{num}/{1}'
            
            # reduce
            _gcd = math.gcd(num, deno)
            return f'{num // _gcd}/{deno // _gcd}'


        def solve(expression: str) -> str:
            start = 1 if expression[0] in operations else 0
            for index in range(start, len(expression)):
                if expression[index] in operations:
                    return evaluate(expression[:index], solve(expression[index:]))

            return expression


        return reduce(solve(expression))
