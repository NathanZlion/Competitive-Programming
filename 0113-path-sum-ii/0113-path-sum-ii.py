# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def traverse(node: TreeNode, remainingSum: int, runningList: List[int]) -> None:
            runningList.append(node.val)
            remainingSum -= node.val

            if not (node.left or node.right):
                if remainingSum == 0:
                    res.append(runningList.copy())

            if node.left:
                traverse(node.left, remainingSum, runningList)

            if node.right:
                traverse(node.right, remainingSum, runningList)

            runningList.pop()
                
        if root:
            traverse(root, targetSum, [])
        
        return res