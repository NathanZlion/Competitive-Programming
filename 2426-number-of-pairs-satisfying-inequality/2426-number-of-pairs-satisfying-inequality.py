class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        difference = [0 for _ in range(n)]
        
        for i in range(n):
            difference[i] = nums1[i] - nums2[i]

        self.pairCount = 0

        def mergeSort(nums: List[int]) -> List[int]:

            if len(nums) == 1:
                return nums

            leftHalf = mergeSort(nums[:len(nums)//2])
            rightHalf = mergeSort(nums[len(nums)//2:])

            ptr2 = 0

            for ptr1 in range(len(leftHalf)):
                while ptr2 < len(rightHalf) and rightHalf[ptr2]+diff < leftHalf[ptr1]:
                    ptr2 += 1

                self.pairCount += len(rightHalf) - ptr2

            return merge(leftHalf, rightHalf)

        
        def merge(arr1: List[int], arr2: List[int]):
            res = []
            
            ptr1 = ptr2 = 0
            while ptr1 < len(arr1) and ptr2 < len(arr2):
                if arr1[ptr1] <= arr2[ptr2]:
                    res.append(arr1[ptr1])
                    ptr1 += 1
                
                else:
                    res.append(arr2[ptr2])
                    ptr2 += 1


            while ptr1 < len(arr1):
                res.append(arr1[ptr1])
                ptr1 += 1

            while ptr2 < len(arr2):
                res.append(arr2[ptr2])
                ptr2 += 1

            return res
    
        mergeSort(difference)
        return self.pairCount



