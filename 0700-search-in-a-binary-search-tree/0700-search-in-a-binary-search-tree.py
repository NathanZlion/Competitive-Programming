class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        curr = root
        while curr:
            if curr.val == val:
                break
            elif curr.val > val:
                curr = curr.left
            else:
                curr = curr.right
        
        return curr
        