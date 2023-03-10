class Solution:

    def numberOfOnes(self, number: int) -> Optional[List[int]]:
        onesCount = 0

        while number:
            onesCount += number%2
            number//=2

        return onesCount


    def countBits(self, n: int) -> List[int]:
        ans = [0 for _ in range(n+1)]
        
        for i in range(n+1):
            ans[i] = self.numberOfOnes(i)

        return ans
        