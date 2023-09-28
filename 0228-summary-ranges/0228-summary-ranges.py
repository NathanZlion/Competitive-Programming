class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        res = []
        stack = []
        for num in nums:
            if len(stack) == 0 or stack[-1] == num - 1:
                stack.append(num)
            else:
                if len(stack) == 1:
                    res.append(str(stack.pop()))
                else:
                    res.append(f'{stack[0]}->{stack[-1]}')
                stack = [num]

        if stack:
            if len(stack) == 1:
                res.append(str(stack.pop()))
            else:
                res.append(f'{stack[0]}->{stack[-1]}')

        return res