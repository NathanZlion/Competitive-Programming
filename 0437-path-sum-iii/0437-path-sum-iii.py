# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        self.sum_ = 0
        dict = defaultdict(int)
        dict[0] = 1
        self.countOfPaths = 0

        def backTrack(node: TreeNode):
            if not node:
                return
            
            self.sum_ += node.val

            self.countOfPaths += dict[self.sum_ - targetSum]
            
            dict[self.sum_] += 1
            backTrack(node.left)
            backTrack(node.right)
            dict[self.sum_] -= 1
            self.sum_ -= node.val
            
        
        backTrack(root)

        return self.countOfPaths
