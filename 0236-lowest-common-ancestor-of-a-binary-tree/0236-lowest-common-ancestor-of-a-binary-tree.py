# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def commonAnsestor(node: 'TreeNode'):
            if node is p or node is q:
                return node
            
            leftRes = rightRes = None
            if node.left:
                leftRes = commonAnsestor(node.left)
            
            if node.right:
                rightRes = commonAnsestor(node.right)
            
            if leftRes and rightRes:
                return node

            return leftRes or rightRes
    
        return commonAnsestor(root)