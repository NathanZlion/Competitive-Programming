class Solution:
    def countPrimes(self, n: int) -> int:
        """using prime sieve counts the number of prime numbers upto n"""
        
        if n < 3:
            return 0

        is_prime = [True for _ in range(n)]
        is_prime[0] = is_prime[1] = False

        i = 2
        while i * i < n:
            if is_prime[i]:
                j = 2 * i

                while j < n:
                    is_prime[j] = False
                    j += i

            i += 1

        count = 0
        for num_is_prime in is_prime:
            if num_is_prime:
                count += 1

        return count