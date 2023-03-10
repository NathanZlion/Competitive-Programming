# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        levels = []

        def backTrack(node, index, depth):
            if not node:
                return
            
            if depth >= len(levels):
                levels.append([index])
            else:
                print(levels[depth])
                if len(levels[depth]) > 1:
                    levels[depth].pop()

                levels[depth].append(index)
                
            backTrack(node.left, index*2, depth+1)
            backTrack(node.right, index*2+1, depth+1)
        
        
        backTrack(root, 0, 0)
        
        maxWidth = -1

        for arr in levels:
            maxWidth = max(maxWidth, arr[-1]-arr[0]+1)
        
        return maxWidth
            
            
            
            
            
            
        