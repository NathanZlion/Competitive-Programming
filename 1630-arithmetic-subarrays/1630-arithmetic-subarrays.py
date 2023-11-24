class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        # brute force approach
        res = []
        def get_diff(arr: List[int]) -> List[int]:
            return [arr[i+1] - arr[i] for i in range(len(arr)-1)]            

        for left, right in zip(l, r):
            sorted_nums = sorted(nums[left: right + 1])
            diff_arr = set(get_diff(sorted_nums))
            
            res.append(len(diff_arr) < 2)

        return res
