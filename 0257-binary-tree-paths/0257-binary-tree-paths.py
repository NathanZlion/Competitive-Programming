# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        self.paths = []
        self.path = [root.val]
        
        def backTrack(node):

            # it is a leaf node
            if not (node.right or node.left):
                self.paths.append("->".join(map(str, self.path)))
                return

            if node.right:
                self.path.append(node.right.val)
                backTrack(node.right)
                self.path.pop()

            if node.left:
                self.path.append(node.left.val)
                backTrack(node.left)
                self.path.pop()

        backTrack(root)

        return self.paths
            
        