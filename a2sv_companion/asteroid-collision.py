class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        
        
        for rock_size in asteroids:
            destroyed = False

            if rock_size < 0:
                while stack and stack[-1] > 0:
                    opponent = stack[-1]

                    if opponent > -rock_size:
                        destroyed = True
                        break

                    elif opponent < -rock_size:
                        stack.pop()

                    else:
                        stack.pop()
                        destroyed = True
                        break

            if not destroyed:
                stack.append(rock_size)

        return stack
