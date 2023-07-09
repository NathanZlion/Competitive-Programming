class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums) if len(set(nums)) == len(nums) else 1

        diff = [-2 for _ in range(len(nums) -1)]

        for index in range(len(nums) -1):
            if nums[index] > nums[index+1]:
                diff[index] = -1

            elif nums[index] < nums[index+1]:
                diff[index] = 1

        memo = {len(nums) : 1}

        def backtrack(index):
            if index in memo:
                return memo[index]
            
            max_next = 0
            for idx in range(index+1, len(diff)):
                # if have opposite sign
                if diff[index] + diff[idx] == 0:
                    max_next = max(max_next, backtrack(idx))

            memo[index] = max_next + 1
            return memo[index]

        for index in range(len(diff)):
            if diff[index] != -2:
                backtrack(index)
        
        if len(memo) == 1:
            return 1
        return max(memo.values()) + 1
