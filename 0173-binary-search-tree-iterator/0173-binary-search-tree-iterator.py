# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        # construct an inorder tracersal during initializaion
        self.traversal = []
        self.inorderTraverse(root)
        self.curr = -1
        
    def inorderTraverse(self, node: Optional[TreeNode]) -> None:
        if (node):
            self.inorderTraverse(node.left)
            self.traversal.append(node.val)
            self.inorderTraverse(node.right)

    def next(self) -> Optional[int]:
        self.curr += 1
        return self.traversal[self.curr]
        

    def hasNext(self) -> bool:
        return self.curr < len(self.traversal)-1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()