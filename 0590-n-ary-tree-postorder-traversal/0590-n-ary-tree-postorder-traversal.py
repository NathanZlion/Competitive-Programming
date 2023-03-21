"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.lst = []
        stack = [root] if root else []

        while stack:
            curr_node = stack.pop()
            self.lst.append(curr_node.val)
            
            for child in curr_node.children:
                
                stack.append(child)
                    
        
        return self.lst[::-1]
        