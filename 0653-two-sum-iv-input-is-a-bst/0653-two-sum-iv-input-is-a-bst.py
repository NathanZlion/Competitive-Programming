# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        
        visited = set()
        def traverse(node: Optional[TreeNode]) -> bool:
            nonlocal visited
            
            if not node:
                return False
            
            if traverse(node.left):
                return True
            
            if (k - node.val) in visited:
                return True
            
            visited.add(node.val)
            if traverse(node.right):
                return True
            
            return False
        
        return traverse(root)
        