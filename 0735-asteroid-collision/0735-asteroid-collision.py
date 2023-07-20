
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:        

        stack = []
        for num in asteroids:
            # if it is positive just append it
            if num > 0:
                stack.append(num)

            elif num < 0:
                should_add = True
                pos_num = -num
                while stack:
                    # if the stack top is positive
                    stack_top = stack[-1]

                    if stack_top < 0:
                        break

                    if stack_top > 0:
                        if pos_num >= stack_top:
                            stack.pop()
                        
                        if pos_num <= stack_top:
                            should_add = False
                            break

                if should_add:
                    stack.append(num)

        return stack
