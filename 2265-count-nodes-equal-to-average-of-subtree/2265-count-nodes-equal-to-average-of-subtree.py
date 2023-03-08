# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def traverse(self, node: Optional[TreeNode]) -> List[int]:
        
        # sum, count

        if not node:
            return [0, 0]

        left_sum, left_count = self.traverse(node.left)
        right_sum, right_count = self.traverse(node.right)
        total_count = left_count + right_count + 1
        total_sum = left_sum + right_sum + node.val
        average = math.floor(total_sum / total_count)

        if node.val == average:
            self.count += 1

        return [total_sum, total_count]

    
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count = 0

        self.traverse(root)
        
        return self.count