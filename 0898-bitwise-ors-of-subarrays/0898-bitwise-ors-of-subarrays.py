class Solution:

    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res, cur = set(), set()
        for num in arr:
            cur = {num | existingNum for existingNum in cur} | {num}
            res |= cur

        return len(res)
