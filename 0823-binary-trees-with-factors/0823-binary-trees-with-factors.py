class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        modulus = 10**9 + 7
        arr.sort()
        arr_set = set(arr)

        @cache
        def dp(num: int) -> int:
            res = 1
            
            for i in arr:
                if i >= num:
                    break

                if num % i != 0:
                    continue

                if num // i in arr_set:
                    res += (dp(i) * dp(num // i))

            return res % modulus

        res = 0
        for num in arr:
            print(num, dp(num))
            res += dp(num)

        return res % modulus
