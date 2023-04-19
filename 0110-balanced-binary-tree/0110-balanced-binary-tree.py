# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # height of the left and right subtree of any node differ by not more than 1.

        if not root:
            return True
        
        isBalanced : bool = True

        def dfs(node: TreeNode) -> int:
            nonlocal isBalanced

            if not node:
                return 0
            
            leftDepth = dfs(node.left) if node.left else 0
            rightDepth = dfs(node.right) if node.right else 0
            
            if abs(rightDepth - leftDepth) > 1:
                isBalanced = False
            
            return max(leftDepth, rightDepth) + 1

        dfs(root)

        return isBalanced
