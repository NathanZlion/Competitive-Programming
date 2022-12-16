class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack=[]
        pushPointer= 0
        popPointer= 0

        while (pushPointer < len(pushed)):
            stack.append(pushed[pushPointer])
            pushPointer+=1

            while (len(stack)!=0) and (stack[-1] == popped[popPointer]):
                stack.pop()
                popPointer+=1
        
        return len(stack)==0
