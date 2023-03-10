class Solution:

    def numberOfOnes(self, number: int) -> Optional[List[int]]:
        onesCount = 0

        while number:
            onesCount += number%2
            number//=2

        return onesCount


    def countBits(self, n: int) -> List[int]:
        ans = []
        
        for i in range(n+1):
            ans.append(self.numberOfOnes(i))

        return ans
        