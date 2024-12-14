class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        freq = {}
        left = right = 0
        count = 0 

        for right in range(len(nums)):
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            while max(freq) - min(freq) > 2:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

            count += right - left + 1

        return count