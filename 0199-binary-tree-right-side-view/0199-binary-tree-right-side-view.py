# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        levels = []
        
        def backTrack(node, depth):

            if not node:
                return
            
            if len(levels) == depth:
                levels.append(node.val)
            else:
                levels[depth] = node.val
            
            backTrack(node.left, depth+1)
            backTrack(node.right, depth+1)
        
        backTrack(root, 0)
        
        return levels