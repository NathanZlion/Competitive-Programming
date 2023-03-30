# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def insertNode(self, parentNode, val):
        if not parentNode:
            return TreeNode(val, None, None)
        
        if parentNode.val < val:
            parentNode.right = self.insertNode(parentNode.right, val)
        
        else:
            parentNode.left = self.insertNode(parentNode.left, val)
        
        return parentNode
        
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        self.root = TreeNode(preorder[0], None, None)
        
        for i in range(1, len(preorder)):
            self.insertNode(self.root, preorder[i])
        
        
        return self.root

    