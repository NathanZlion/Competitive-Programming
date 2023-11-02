# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def traverse(node: TreeNode) -> Tuple[int, int, int]:
            """(subtree_sum, subtree_count, res_count)"""
            # base case
            if not node:
                return (0, 0, 0)
            
            left_subtree_sum, left_subtree_count, left_res_count = traverse(node.left)
            right_subtree_sum, right_subtree_count, right_res_count = traverse(node.right)
            
            res_count = left_res_count + right_res_count
            subtree_count = left_subtree_count + right_subtree_count + 1
            subtree_sum = left_subtree_sum + right_subtree_sum + node.val
            
            if subtree_sum // subtree_count == node.val:
                res_count += 1
            
            return (subtree_sum, subtree_count, res_count)
        
        return traverse(root)[2]
