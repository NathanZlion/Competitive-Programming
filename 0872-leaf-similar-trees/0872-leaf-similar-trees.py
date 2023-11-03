# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def collect_leaves(node, tree_leaves):
            if not node:
                return
            
            collect_leaves(node.left, tree_leaves)
            collect_leaves(node.right, tree_leaves)
            
            if not (node.left or node.right):
                tree_leaves.append(node.val)
        
        tree1_leaves = []
        collect_leaves(root1, tree1_leaves)
        
        tree2_leaves = []
        collect_leaves(root2, tree2_leaves)
        
        return tree1_leaves == tree2_leaves
