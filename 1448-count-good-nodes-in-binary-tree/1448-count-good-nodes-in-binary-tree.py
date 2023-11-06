# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def traverse(node: TreeNode, runn_max: int):
            if not node:
                return 0

            res = 0
            if node.val >= runn_max:
                res += 1
            
            runn_max = max(runn_max, node.val)

            return res + traverse(node.left, runn_max) + traverse(node.right, runn_max)

        return traverse(root, -inf)
