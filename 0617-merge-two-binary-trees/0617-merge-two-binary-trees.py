# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        if not (root1 or root2):
            return None

        elif root1 and root2:
            root1.val += root2.val
            root1.right = self.mergeTrees(root1.right, root2.right)
            root1.left = self.mergeTrees(root1.left, root2.left)
            return root1

        elif root2:
            return root2
        
        return root1
