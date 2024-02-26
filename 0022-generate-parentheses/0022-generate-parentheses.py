class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        # backtrack your way into the soluton
        def backtrack(parentheses, openingLeft, closingLeft):
            if closingLeft < openingLeft or closingLeft < 0 or openingLeft < 0:
                return
            
            if closingLeft == openingLeft == 0:
                output.append("".join(parentheses))
                return
            
            parentheses.append("(")
            backtrack(parentheses, openingLeft - 1, closingLeft)
            parentheses.pop()

            parentheses.append(")")
            backtrack(parentheses, openingLeft, closingLeft - 1)
            parentheses.pop()

        backtrack(parentheses = [], openingLeft = n, closingLeft = n)
        return output
