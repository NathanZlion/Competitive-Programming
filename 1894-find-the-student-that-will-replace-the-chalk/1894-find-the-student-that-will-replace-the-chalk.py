class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)
        for index, chalksUsed in enumerate(chalk):
            if chalksUsed > k:
                return index
            
            k -= chalksUsed