class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ptr = 0
        res = []
        while ptr < len(s):
            if ptr + k < len(s):
                res.append(s[ptr:ptr+k][::-1])
                res.append(s[ptr+k:ptr+2*k])
            else:
                res.append(s[ptr:][::-1])
                break
            ptr += 2*k
        
        return "".join(res)
