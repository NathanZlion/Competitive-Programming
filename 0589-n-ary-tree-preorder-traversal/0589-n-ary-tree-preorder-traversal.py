"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
        
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        self.lst = []
        stack = [root]

        while stack:
            curr_node = stack.pop()
            self.lst.append(curr_node.val)
            for index in range(len(curr_node.children)-1,-1,-1):
                
                stack.append(curr_node.children[index])
            
        return self.lst
    