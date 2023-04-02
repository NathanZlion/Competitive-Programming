

class Solution:

    def mergeSort(self, arr: Optional[List[Tuple[int, int]]]) -> Optional[List[Tuple[int, int]]]:
        if len(arr) < 2:
            return arr

        return self.merge(self.mergeSort(arr[:len(arr)//2]), self.mergeSort(arr[len(arr)//2: ]))


    def merge(self, leftHalf: Optional[List[Tuple[int, int]]], rightHalf : Optional[List[Tuple[int, int]]]) -> Optional[List[Tuple[int, int]]]:

        right = -1
        for left in range(len(leftHalf)):
            while right < len(rightHalf)-1 and rightHalf[right+1][0] < leftHalf[left][0]:
                right += 1

            self.count[leftHalf[left][1]] += right+1
        
        res = []
        left = 0
        right = 0
        
        while left < len(leftHalf) and right < len(rightHalf):
            if leftHalf[left][0] < rightHalf[right][0]:
                res.append(leftHalf[left])
                left += 1
            
            else:
                res.append(rightHalf[right])
                right += 1
        
        while left < len(leftHalf):
            res.append(leftHalf[left])
            left += 1

        while right < len(rightHalf):
            res.append(rightHalf[right])
            right += 1

        return res


    def countSmaller(self, nums: List[int]) -> List[int]:

        self.count = [0 for _ in range(len(nums))]
        numsWithIndex = []

        numsWithIndex = [tuple([nums[index], index]) for index in range(len(nums))]
        self.mergeSort(numsWithIndex)

        return self.count
        
