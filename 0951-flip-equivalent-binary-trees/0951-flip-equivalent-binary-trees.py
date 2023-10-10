# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def areEquivalent(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            # both are none
            if not node1 and not node2:
                return True
            
            # only one of them has a node and the other is none
            if not (node1 and node2):
                return False
            
            if node1.val == node2.val:
                # swapped or not swapped
                return (
                    areEquivalent(node1.left, node2.left) and areEquivalent(node1.right, node2.right) or
                    areEquivalent(node1.left, node2.right) and areEquivalent(node1.right, node2.left)
                )
            
            return False
        
        return areEquivalent(root1, root2)
