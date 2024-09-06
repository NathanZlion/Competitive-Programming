class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [None for _ in range(len(s))]
        
        for i, index in enumerate(indices):
            res[index] = s[i]
        
        return "".join(res)
