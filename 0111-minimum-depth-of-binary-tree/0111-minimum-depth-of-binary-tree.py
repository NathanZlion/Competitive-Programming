# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def minimum_depth_of(node: TreeNode) -> int:
            if not node.left and node.right:
                return 1 + minimum_depth_of(node.right)
            
            if not node.right and node.left:
                return 1 + minimum_depth_of(node.left)
            
            if not (node.left or node.right):
                return 1
            
            return min(minimum_depth_of(node.left), minimum_depth_of(node.right)) + 1
                
        
        return minimum_depth_of(root)