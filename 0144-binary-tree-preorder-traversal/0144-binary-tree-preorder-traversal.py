
class Solution:
    
    def traverse(self, node: TreeNode) -> None:
        if node:
            self.values.append(node.val)
            self.traverse(node.left)
            self.traverse(node.right)
        

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.values = []
        self.traverse(root)
        return self.values

