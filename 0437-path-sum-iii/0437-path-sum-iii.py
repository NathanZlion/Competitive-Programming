# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        self.prefix_sum = 0
        dict = defaultdict(lambda: 0)
        dict[0] = 1
        self.countOfPaths = 0

        def backTrack(node: TreeNode):
            if not node:
                return
            
            self.prefix_sum += node.val
            self.countOfPaths += dict[self.prefix_sum - targetSum]
            dict[self.prefix_sum] += 1
            
            backTrack(node.left)
            backTrack(node.right)
            
            dict[self.prefix_sum] -= 1
            self.prefix_sum -= node.val
            
        
        backTrack(root)

        return self.countOfPaths
