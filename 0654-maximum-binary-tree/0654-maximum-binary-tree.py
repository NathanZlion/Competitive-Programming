# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxNumIndex(self, nums: List[int], left: int, right: int) -> int:
        currMaxIndex = left
        for index in range(left, right + 1):
            if nums[currMaxIndex] < nums[index]:
                currMaxIndex = index
        
        return currMaxIndex


    def constructTree(self, nums: list[int], left: int, right: int) -> Optional[TreeNode]:
        if right < left:
            return None

        maxIndex = self.maxNumIndex(nums, left, right)
        maxValue = nums[maxIndex]
        res = TreeNode(maxValue)
                
        res.right = self.constructTree(nums, maxIndex + 1, right)
        res.left = self.constructTree(nums, left, maxIndex - 1)

        return res


    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.constructTree(nums, 0, len(nums) - 1)
