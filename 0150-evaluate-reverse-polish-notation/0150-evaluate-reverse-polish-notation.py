class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {'+','-','*','/'}
        
        stack = []
        
        for val in tokens:
            if val in operations:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(int(eval(str(op1)+val+str(op2))))
            else:
                stack.append(int(val))

        return stack[-1]
                
                    
                    
                


