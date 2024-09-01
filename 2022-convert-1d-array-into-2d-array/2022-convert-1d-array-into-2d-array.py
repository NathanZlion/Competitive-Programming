class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # empty array  returned if impossible
        arrayLen = len(original)
        if arrayLen != m * n:
            return []
        
        res = [[0]*n for _ in range(m)]
        for index, val in enumerate(original):
            row = index // n
            col = index % n
            res[row][col] = val

        return res
