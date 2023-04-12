# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        totalSum = 0
        pathSum = 0

        def dfs(node: Optional[TreeNode]):
            nonlocal pathSum
            nonlocal totalSum

            pathSum *= 10
            pathSum += node.val

            if node.left:
                dfs(node.left)

            if node.right:
                dfs(node.right)

            if not (node.left or node.right):
                totalSum += pathSum

            pathSum -= node.val
            pathSum //= 10

        dfs(root)

        return totalSum

