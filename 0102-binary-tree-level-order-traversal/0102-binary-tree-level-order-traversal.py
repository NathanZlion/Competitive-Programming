# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def traverse(self, root: Optional[TreeNode], depth: int) -> None:
        if not root:
            return 

        if depth >= len(self.traversedList):
            self.traversedList.append([root.val])

        else:
            self.traversedList[depth].append(root.val)

        self.traverse(root.left, depth+1)
        self.traverse(root.right, depth+1)


    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.traversedList = []
        self.traverse(root,0)


        return self.traversedList