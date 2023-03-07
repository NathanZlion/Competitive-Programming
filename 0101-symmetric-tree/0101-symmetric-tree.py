# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> True:
        if not (root1 or root2):
            return True
        
        if not (root1 and root2):
            return False
        
        return self.isSimilar(root1.right, root2.right) and root1.val == root2.val and self.isSimilar(root1.left, root2.left)
            

    def invert(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        root.right, root.left = self.invert(root.left), self.invert(root.right)
        
        return root
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.isSimilar(root.left, self.invert(root.right))
        
        