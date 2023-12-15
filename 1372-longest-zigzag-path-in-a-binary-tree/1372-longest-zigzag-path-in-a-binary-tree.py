# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        longest_path_length = 0
        
        def traverse(node: Optional[TreeNode]):
            nonlocal longest_path_length
 
            if not node:
                return 0, 0

            _, right_moves = traverse(node.left)
            left_moves, _ = traverse(node.right)
            left_moves += 1
            right_moves += 1

            longest_path_length = max(longest_path_length, right_moves, left_moves)
            return  right_moves, left_moves

        traverse(root)
        return max(longest_path_length - 1, 0)
