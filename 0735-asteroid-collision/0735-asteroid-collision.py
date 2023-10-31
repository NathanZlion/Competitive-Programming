class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for asteroid in asteroids:
            destroyed = False
            # moving left
            if asteroid < 0:
                while stack:
                    # moving in the same direction
                    if stack[-1] < 0:
                        break

                    if stack[-1] > -asteroid:
                        destroyed = True
                        break
                    
                    if stack[-1] == -asteroid:
                        stack.pop()
                        destroyed = True
                        break
                    
                    stack.pop()

            if not destroyed:
                stack.append(asteroid)
        
        return stack
