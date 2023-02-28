class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        sorted_position = []
        n = len(position)
        for i in range(n):
            sorted_position.append([position[i], speed[i]])
            
        sorted_position.sort(key = lambda x: x[0])
        
        for i in range(n):
            sorted_position[i] = (target-sorted_position[i][0])/sorted_position[i][1]

        mono_stack = []
        
        for position in sorted_position[::-1]:
            if not mono_stack or mono_stack[-1] < position:
                mono_stack.append(position)

        return len(mono_stack)
                
                
