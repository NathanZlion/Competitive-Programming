class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = [[0] * len(piles) for _ in range(len(piles))]
        suffix_sum = piles[:]

        for i in range(len(suffix_sum) - 2, -1, -1):
            suffix_sum[i] += suffix_sum[i + 1]

        return self.max_stones(suffix_sum, 1, 0, memo)

    def max_stones(
        self,
        suffix_sum: List[int],
        max_till_now: int,
        curr_index: int,
        memo: List[List[int]],
    ) -> int:
        if curr_index + 2 * max_till_now >= len(suffix_sum):
            return suffix_sum[curr_index]

        if memo[curr_index][max_till_now] > 0:
            return memo[curr_index][max_till_now]

        res = float("inf")

        for i in range(1, 2 * max_till_now + 1):
            res = min(
                res,
                self.max_stones(
                    suffix_sum,
                    max(i, max_till_now),
                    curr_index + i,
                    memo,
                ),
            )

        memo[curr_index][max_till_now] = suffix_sum[curr_index] - res
        return memo[curr_index][max_till_now]
