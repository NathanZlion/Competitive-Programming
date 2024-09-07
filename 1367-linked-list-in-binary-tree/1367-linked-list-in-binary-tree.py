class Solution:
    def isSubPath(
        self, head: Optional[ListNode], root: Optional[TreeNode]
    ) -> bool:
        if not root:
            return False
        # Check the current node and all its descendants
        # Check all paths from the left and right children of the root

        return self.dfs(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def dfs(self, node: Optional[TreeNode], head: Optional[ListNode]) -> bool:
        if not head:
            return True

        if not node:
            return False

        return (node.val == head.val) and (self.dfs(node.left, head.next) or self.dfs(node.right, head.next))
