# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        self.levels = []

        def backTrack(node : Optional[TreeNode], depth: int) -> bool:

            if depth >= len(self.levels):
                self.levels.append([node.val if node else None])

            else:
                self.levels[depth].append(node.val if node else None)
            
            if node and len(self.levels[depth]) > 1 and not self.levels[depth][-2]:
                return False

            if node:
                if not backTrack(node.left, depth+1):
                    return False
                
                if not backTrack(node.right, depth+1):
                    return False

            return True

        def isValid(levels: List[List[int or None]]) -> bool:
            for i in range(len(levels)-1):
                if len(levels[i]) != 2**i:
                    return False
            
            return True
    
        
        if backTrack(root,0) and isValid(self.levels):
            return True

        return False
    
    
    
    
    
    
    