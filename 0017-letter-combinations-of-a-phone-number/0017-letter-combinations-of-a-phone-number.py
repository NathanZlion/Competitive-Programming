class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # for every digit in the digits do backtracking
        combinations = []        
        digitToAlpha = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        queue = deque()
        queue.append(([], 0))

        while len(queue) > 0:
            for _ in range(len(queue)):
                comb, index = queue.pop()
                digit = digits[index]

                for alphabet in digitToAlpha[digit]:
                    comb.append(alphabet)

                    if len(comb) == len(digits):
                        combinations.append(''.join(comb))
                    else:
                        queue.append((comb.copy(), index + 1))

                    comb.pop()

        return combinations
