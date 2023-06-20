class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # need a memo dictionary
        memo = {}
        
        # base case out of range returns 0
        number_of_homes = len(nums)
        
        def max_loot(house_number, house_zero = False):
            nonlocal number_of_homes
            
            if house_number >= number_of_homes:
                return 0
            
            # if started at house zero avoid visiting the last home as it is adjecant to house 0
            if house_zero and house_number == number_of_homes - 1:
                return 0

            if house_number in memo:
                return memo[house_number]

            memo[house_number] = nums[house_number] + max(max_loot(house_number + 2, house_zero), max_loot(house_number + 3, house_zero))

            return memo[house_number]

        if len(nums) < 4:
            return max(nums)
        
        first_possibility = max_loot(0, True)
        memo.clear()
        second_possibility = max_loot(1, False)
        memo.clear()
        third_possibility = max_loot(2, False)


        return max(first_possibility, second_possibility, third_possibility)