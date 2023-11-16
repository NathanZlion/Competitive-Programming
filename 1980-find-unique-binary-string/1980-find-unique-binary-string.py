class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        max_num = pow(2, n)
        num_set = set()
        
        for bin_str in nums:
            num_set.add(int(bin_str, 2))

        for i in range(max_num):
            if i not in num_set:
                return str(bin(i)[2:]).zfill(n)
