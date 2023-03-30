class Solution:
    def findComplement(self, num: int) -> int:
        binaries = []
        
        while num:
            binaries.append(num%2)
            num //= 2
        
        res = 0
        while binaries:
            res<<=1
            res += 0 if binaries.pop() else 1
        
        
        return res