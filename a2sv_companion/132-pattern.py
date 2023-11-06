class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        s3 = float('-inf')

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < s3:
                return True
            else:
                while stack and nums[i] > stack[-1]:
                    s3 = stack.pop()
                stack.append(nums[i])

        return False