class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def max_loot(house_num, end_house):

            if house_num > end_house:
                return 0

            if house_num not in memo:
                memo[house_num] = nums[house_num]
                memo[house_num] += max(max_loot(house_num+2, end_house), max_loot(house_num+3, end_house))

            return memo[house_num]

        if len(nums) < 4:
            return max(nums)

        first_possiblilty = max_loot(0, len(nums)-2)
        memo.clear()
        second_possibility = max_loot(1, len(nums)-1)
        memo.clear()
        third_possibility = max_loot(2, len(nums)-1)

        return max(first_possiblilty, second_possibility, third_possibility)
