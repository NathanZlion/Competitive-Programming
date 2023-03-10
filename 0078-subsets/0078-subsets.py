class Solution:
    
    def backTrace(self, arr:List[int], index:int):

        if index == len(self.nums):
            self.allSubsets.append(arr)
            return

        self.backTrace(arr, index+1)
        newarr = [i for i in arr]
        newarr.append(self.nums[index])
        self.backTrace(newarr, index+1)


    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.allSubsets = []
        self.backTrace([], 0)

        return self.allSubsets
        