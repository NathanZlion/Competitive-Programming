# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def traverse(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        self.traverse(root.left)
        self.inorderTraversal.append(root.val)
        self.traverse(root.right)

        if len(self.inorderTraversal) >= self.k:
            return


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.inorderTraversal = []
        self.k = k
        self.traverse(root)
        
        return self.inorderTraversal[k-1]
        