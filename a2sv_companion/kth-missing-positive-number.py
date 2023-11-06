class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        num = 1
        ptr2 = 0

        while True:
            # find the first missing number
            while ptr2 < len(arr) and num == arr[ptr2]:
                num += 1
                ptr2 += 1

            k -= 1
            if k == 0:
                return num
            
            num += 1
