class Solution:
    def nearestPalindromic(self, n: str) -> str:
        len_n = len(n)
        i = len_n // 2 if len_n % 2 == 0 else len_n // 2 + 1
        first_half = int(n[:i])
        """
        Generate possible palindromic candidates:
        1. Create a palindrome by mirroring the first half.
        2. Create a palindrome by mirroring the first half incremented by 1.
        3. Create a palindrome by mirroring the first half decremented by 1.
        4. Handle edge cases by considering palindromes of the form 999... 
           and 100...001 (smallest and largest n-digit palindromes).
        """
        possibilities = []
        possibilities.append(
            self.half_to_palindrome(first_half, len_n % 2 == 0)
        )
        possibilities.append(
            self.half_to_palindrome(first_half + 1, len_n % 2 == 0)
        )
        possibilities.append(
            self.half_to_palindrome(first_half - 1, len_n % 2 == 0)
        )
        possibilities.append(10 ** (len_n - 1) - 1)
        possibilities.append(10**len_n + 1)

        diff = float("inf")
        res = 0
        nl = int(n)
        for cand in possibilities:
            if cand == nl:
                continue
            if abs(cand - nl) < diff:
                diff = abs(cand - nl)
                res = cand
            elif abs(cand - nl) == diff:
                res = min(res, cand)
        return str(res)

    def half_to_palindrome(self, left: int, even: bool) -> int:
        res = left
        if not even:
            left //= 10

        while left > 0:
            res = res * 10 + left % 10
            left //= 10

        return res
