# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def recursive(node: TreeNode | None, canPick: bool) -> int:
            if not node:
                return 0

            if (node, canPick) in memo:
                return memo[(node, canPick)]

            if not canPick:
                memo[(node, canPick)] = recursive(node.left, not canPick) + recursive(node.right, not canPick)

            elif canPick:
                memo[(node, canPick)] = max(
                    node.val + recursive(node.left, not canPick) + recursive(node.right, not canPick),
                    recursive(node.left, canPick) + recursive(node.right, canPick)
                )

            return memo[(node, canPick)]

        return max(recursive(root, canPick = True), recursive(root, canPick = False))
