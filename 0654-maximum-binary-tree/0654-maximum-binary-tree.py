# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        maxValue = max(nums)
        res = TreeNode(maxValue)
        
        index = nums.index(maxValue)
        res.right = self.constructMaximumBinaryTree(nums[index+1:])
        res.left = self.constructMaximumBinaryTree(nums[:index])

        return res