class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_index_map = {}

        for i, num in enumerate(nums):
            comp = target - num

            if comp in complement_index_map:
                return [complement_index_map[comp], i]

            complement_index_map[num] = i