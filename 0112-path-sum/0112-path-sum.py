# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root: return False
        
        def dfs(node: TreeNode, currSum = 0) -> bool:
            currSum += node.val

            # reached a leaf node
            if not (node.left or node.right):
                return currSum == targetSum
            
            if node.left:
                if dfs(node.left, currSum):
                    return True
            
            if node.right:
                if dfs(node.right, currSum):
                    return True
                
            return False
            
        
        
        return dfs(root)