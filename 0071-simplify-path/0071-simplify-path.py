class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.replace('//','/').split('/')
        stack = []
        
        for pth in path:
            if pth == '' or pth == '.':
                continue
            elif pth == '..':
                if stack: stack.pop()
            
            else:
                stack.append(pth)
        
        return "/"+"/".join(stack)
        