class Solution:
    def merge(self, leftArr, rightArr):
        res = [0] * (len(leftArr) + len(rightArr))
        ptr1 = ptr2 = ptr3 = 0
        while ptr1 < len(leftArr) and ptr2 < len(rightArr):
            if leftArr[ptr1] > rightArr[ptr2]:
                res[ptr3] = rightArr[ptr2]
                ptr2 += 1
            else:
                res[ptr3] = leftArr[ptr1]
                ptr1 += 1

            ptr3 += 1
        
        while ptr1 < len(leftArr):
            res[ptr3] = leftArr[ptr1]
            ptr1 += 1
            ptr3 += 1
        
        while ptr2 < len(rightArr):
            res[ptr3] = rightArr[ptr2]
            ptr2 += 1
            ptr3 += 1

        return res

    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length <= 1:
            return nums
        
        leftArr = self.sortArray(nums[:length//2])
        rightArr = self.sortArray(nums[length//2:])
        

        return self.merge(leftArr, rightArr)
