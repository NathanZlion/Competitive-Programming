class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        parity = [(nums[i] + nums[i+1]) % 2 for i in range(len(nums) - 1)]
        
        # do a prefix sum on the parity
        for i in range(1, len(parity)):
            parity[i] += parity[i-1]
        
        parity.append(0)

        res = [
            parity[right - 1] - parity[left - 1] == (right - left)
            for left, right in queries
        ]
        
        return res
