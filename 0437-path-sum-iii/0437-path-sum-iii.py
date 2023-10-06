# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:        
        count = 0
        prefixSum = defaultdict(int)
        prefixSum[0] = 1

        def traverse(node, runningSum) -> None:
            nonlocal count

            if not node:
                return 

            runningSum += node.val
            count += prefixSum[runningSum - targetSum]
            prefixSum[runningSum] += 1

            traverse(node.left, runningSum)
            traverse(node.right, runningSum)
            
            prefixSum[runningSum] -= 1

        traverse(root, 0)

        return count