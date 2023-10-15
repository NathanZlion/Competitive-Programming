class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        subarray_count = 0

        remainder_count = defaultdict(int)
        remainder_count[0] = 1
        running_sum = 0

        for index in range(n):
            running_sum += nums[index]
            curr_remainder = running_sum % k
            needed_remainder = (curr_remainder -k)%k
            subarray_count += remainder_count[needed_remainder]
            remainder_count[curr_remainder] += 1

        return subarray_count