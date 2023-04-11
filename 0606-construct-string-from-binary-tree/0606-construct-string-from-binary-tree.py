# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def explore(node):
            
            if not node:
                return False

            left = explore(node.left) if node.left else None
            right = explore(node.right) if node.right else None

            nodeStr = str(node.val)
            if left or right:
                if left:
                    nodeStr += '(' + left + ')'
                else:
                    nodeStr += '()'
            
            if right:
                nodeStr += '(' + right + ')'

            return nodeStr

        
        return explore(root)