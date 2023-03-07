# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        check the value it self.
        check for right subtree similarity
        check for left subtree similarity
        '''
        
        if not (p or q):
            return True
        
        if p and q:
            return (p.val == q.val) and (self.isSameTree(p.right, q.right)) and (self.isSameTree(p.left, q.left))
        
        return False