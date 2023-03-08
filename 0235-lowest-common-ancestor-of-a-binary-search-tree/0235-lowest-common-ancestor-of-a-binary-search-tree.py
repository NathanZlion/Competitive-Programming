# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def hasNode(self, root: Optional[TreeNode], node: [TreeNode]) -> bool:
        if not (root and node):
            return False

        if root is node:
            return True

        return self.hasNode(root.right, node) or self.hasNode(root.left, node)    


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if self.hasNode(root.right, p) and self.hasNode(root.right, q):
            return self.lowestCommonAncestor(root.right, p, q)

        if self.hasNode(root.left, p) and self.hasNode(root.left, q):
            return self.lowestCommonAncestor(root.left, p, q)
        
        return root
        
        