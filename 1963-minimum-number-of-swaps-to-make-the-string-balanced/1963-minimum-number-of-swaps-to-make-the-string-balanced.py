class Solution:
    def minSwaps(self, s: str) -> int:
        stack_size = 0
        for ch in s:
            # If character is opening bracket, increment the stack size.
            if ch == "[":
                stack_size += 1

            # if it's a closing bracket and we have opening ones in our
            # stack decrement stack size
            elif stack_size > 0:
                stack_size -= 1

        return (stack_size + 1) // 2
