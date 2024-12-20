# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        queue = deque([root])
        level = 0
        
        while queue:
            nodesInLevel = []
            for _ in range(len(queue)):
                currNode = queue.popleft()
                if level % 2:
                    nodesInLevel.append(currNode)

                if currNode.left:
                    queue.append(currNode.left)
                    queue.append(currNode.right)
                
            if level % 2:
                # reverse the nodes in level
                numNodesInLevel = len(nodesInLevel)
                for index in range(numNodesInLevel // 2):
                    leftNode = nodesInLevel[index]
                    rightNode = nodesInLevel[numNodesInLevel - index - 1]
                    temp = rightNode.val
                    rightNode.val = leftNode.val
                    leftNode.val = temp

            level += 1
        return root
