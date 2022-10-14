class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            try:
                stack.append(int(tokens[i]))
            except:
                second = stack.pop()
                first = stack.pop() 
                stack.append(int(eval(str(first) + tokens[i] + str(second))))
        
        return stack.pop()
