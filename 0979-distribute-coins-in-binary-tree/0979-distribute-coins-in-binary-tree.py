# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        moves = 0
        
        def traverse(node: Optional[TreeNode]) -> int:
            nonlocal moves

            if not node:
                return 0
            
            leftRes = traverse(node.left)
            rightRes = traverse(node.right)

            moves += abs(leftRes)
            moves += abs(rightRes)

            return node.val - 1 + leftRes + rightRes
        
        traverse(root)
        return moves