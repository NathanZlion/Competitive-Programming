# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        return [sum(r)/len(r) for r in self.levelOrder(root)]
        
        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        res =  []        
        queue = deque()
        queue.append(root)
        temp = []
        while len(queue) > 0:
            temp.clear()
            currIteration = len(queue)

            for _ in range(currIteration):
                curr = queue.popleft()
                temp.append(curr.val)

                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)

            res.append(temp.copy())
        
        
        return res
        