"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    
    def traverse(self,node):
        # append node if node
        # traverse it's children left to right
        if not node:
            return
        
        self.lst.append(node.val)
        
        for child in node.children:
            self.traverse(child)
        
    def preorder(self, root: 'Node') -> List[int]:
        self.lst = []
        self.traverse(root)
        return self.lst