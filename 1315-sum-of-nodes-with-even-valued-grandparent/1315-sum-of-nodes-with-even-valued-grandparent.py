# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        pathList = []
        evenGrandpaSum = 0
        
        def dfs(node: TreeNode):
            nonlocal evenGrandpaSum

            if len(pathList) > 1 and pathList[-2] % 2 ==0:
                evenGrandpaSum += node.val

            pathList.append(node.val)

            if node.left: dfs(node.left)
            if node.right: dfs(node.right)

            pathList.pop()

        dfs(root)


        return evenGrandpaSum
