# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def traverse(self, node: TreeNode) -> None:
        if node:
            self.traverse(node.left)
            self.traverse(node.right)
            self.values.append(node.val)
        

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.values = []
        self.traverse(root)
        return self.values

