class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        nums_length = len(nums)
        
        @cache
        def dp(index, is_increasing):
            if index == nums_length:
                return 0
            
            max_res = 1
            for next_index in range(index + 1, nums_length):
                if is_increasing and nums[next_index] > nums[index]:
                    max_res = max(max_res, 1 + dp(next_index, not is_increasing))
                elif (not is_increasing) and nums[next_index] < nums[index]:
                    max_res = max(max_res, 1 + dp(next_index, not is_increasing))

            return max_res

        nums.append(-1)
        max_res = dp(-1, True) - 1
        nums[-1] = 1001
        max_res = max(max_res, dp(-1, False) - 1)

        return max_res
