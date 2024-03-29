# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findMaxPathSum(self, node: TreeNode):
        if not node:
            return 0

        leftMax =  self.findMaxPathSum(node.left)
        rightMax =  self.findMaxPathSum(node.right)

        self.currMax = max(self.currMax, node.val, node.val + leftMax, node.val + rightMax, node.val + rightMax + leftMax)

        return max(node.val, node.val+rightMax, node.val+leftMax)

        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.currMax = -float('inf')
        self.findMaxPathSum(root)

        return self.currMax