"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    
    def depth(self, node: 'Node', currDepth: int) -> int:
        if not node:
            return currDepth

        maxDepth = currDepth + 1

        for neighbor in node.children:
            maxDepth = max(self.depth(neighbor, currDepth +1), maxDepth)
        
        return maxDepth

        

    def maxDepth(self, root: 'Node') -> int:
        return self.depth(root, 0)
        
    
        