# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def getListOfValues(node: Optional[TreeNode]) -> int:
            if node is None:
                return []

            res = [node.val]
            res.extend(getListOfValues(node.left))
            res.extend(getListOfValues(node.right))
            
            return res

        arr = list(set(getListOfValues(root)))
        arr.sort()

        if arr.__len__() > 1:
            return arr[1]
        else:
            return -1