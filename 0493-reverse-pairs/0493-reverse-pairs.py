class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        numberOfPairs = 0

        def numOfPairs(arr: List[int]) -> int:
            nonlocal numberOfPairs

            # basecase
            if len(arr) < 2:
                return arr

            mid = len(arr) // 2
            leftArr  = numOfPairs(arr[:mid])
            rightArr = numOfPairs(arr[mid:])

            j = -1
            # formula : 2 * nums[j] < nums[i]
            # count reverse pairs from leftArr to rightArr using 2 pointer
            for i in range(len(leftArr)):
                while j < len(rightArr) - 1 and 2 * rightArr[j+1] < leftArr[i]:
                    j += 1

                numberOfPairs += (j + 1)

            # return merged arr of the 2 halves
            return merge(leftArr, rightArr)


        def merge(lst1: List[int], lst2: List[int]) -> List[int]:
            ptr1 = 0
            ptr2 = 0
            mergedLen = len(lst1) + len(lst2) 
            res = [0 for _ in range(mergedLen)]

            for resPtr in range(mergedLen):
                if ptr1 == len(lst1):
                    res[resPtr] = lst2[ptr2]
                    ptr2 += 1

                elif ptr2 == len(lst2) or lst1[ptr1] < lst2[ptr2]:
                    res[resPtr] = lst1[ptr1]
                    ptr1 += 1

                else:
                    res[resPtr] = lst2[ptr2]
                    ptr2 += 1

            return res


        numOfPairs(nums)

        return numberOfPairs
