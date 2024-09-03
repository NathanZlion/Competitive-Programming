class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res = [str(ord(char) - ord('a') + 1) for char in s]
        res = "".join(res)

        for _ in range(k):
            nextRes = 0
            for char in res:
                nextRes += int(char)

            res = str(nextRes)

        return int(res)
