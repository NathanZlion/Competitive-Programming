# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        self.depths = set()
        self.depth = 1
        
        def backTrack(node):
            
            if not node:
                return 

            if not (node.right or node.left):
                self.depths.add(self.depth)
            
            self.depth += 1
            backTrack(node.right)
            backTrack(node.left)
            self.depth -= 1
            
        backTrack(root)

        return min(self.depths) if self.depths else 0
