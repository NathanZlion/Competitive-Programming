# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @staticmethod
    def isSorted(arr: List[int]) -> bool:
        for i in range(len(arr)-1):
            if arr[i] >= arr[i+1]:
                return False

        return True


    def traverse(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        self.traverse(root.left)
        self.inorderTraversal.append(root.val)
        self.traverse(root.right)


    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        self.inorderTraversal = []
        self.traverse(root)


        return Solution.isSorted(self.inorderTraversal)