# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def helper(self, cur, par, val):
        if not cur:
            if val > par.val:
                par.right = TreeNode(val)
            else:
                par.left = TreeNode(val)

        elif val > cur.val:
            self.helper(cur.right, cur, val)

        else:
            self.helper(cur.left, cur, val)


    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            root =  TreeNode(val)
            return root
        
        self.helper(root, root, val)

        return root

