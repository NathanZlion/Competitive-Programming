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
            self.values.append(node.val)
            self.traverse(node.right)
        

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.values = []
        self.traverse(root)
        return self.values
        
        