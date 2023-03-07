# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            root =  TreeNode(val)
            return root
        
        def helper(cur, par = None):
            if not cur:
                if val > par.val:
                    par.right = TreeNode(val)
                else:
                    par.left = TreeNode(val)
                    
                return
            
            if val > cur.val:
                helper(cur.right, cur)
            elif val < cur.val:
                helper(cur.left, cur)
                
        helper(root)
        return root

        