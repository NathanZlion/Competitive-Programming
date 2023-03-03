class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        n = len(nums)
        
        stack = []
        next_greater_at_index = {}

        for index in range(2*n):
            ind = index%n
            while stack and stack[-1][1] < nums[ind]:
                if not stack[-1][0] in next_greater_at_index:
                    next_greater_at_index[stack.pop()[0]] = nums[ind]

            stack.append([index, nums[ind]])


        next_greater_at_index = defaultdict(lambda:-1, next_greater_at_index )
        for index in range(n):
            nums[index] = next_greater_at_index[index]

        return nums
