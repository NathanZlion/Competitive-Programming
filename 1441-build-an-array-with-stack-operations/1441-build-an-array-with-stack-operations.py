class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ptr = 0
        res = []

        for num in range(1, n+1):
            res.append("Push")

            if num != target[ptr]:
                res.append("Pop")
            else:
                ptr += 1
            
            if ptr == len(target):
                return res

        return res