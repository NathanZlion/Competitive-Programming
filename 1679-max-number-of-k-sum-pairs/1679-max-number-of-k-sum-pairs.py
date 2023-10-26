class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left_ptr, right_ptr = 0, n-1
        nums.sort()
        pair_count = 0

        while right_ptr > left_ptr:
            curr_pair_sum = nums[left_ptr] + nums[right_ptr]
            if curr_pair_sum > k:
                right_ptr -= 1
            elif curr_pair_sum < k:
                left_ptr += 1
            else:
                pair_count += 1
                right_ptr -= 1
                left_ptr += 1

        return pair_count
