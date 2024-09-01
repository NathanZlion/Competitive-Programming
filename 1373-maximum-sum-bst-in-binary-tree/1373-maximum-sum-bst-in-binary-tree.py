# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:        
        maxSum = 0
        maxSumNode = None
        NEG_INF = float("-inf")
        INF = float("inf")

        def traverse(node: Optional[TreeNode], lowerBound: int, upperBound: int) -> [bool, int, int, int]:
            nonlocal maxSum, maxSumNode
            
            if not node:
                return True, 0, INF, NEG_INF
            

            isLeftSubtreeBST, leftSubTreeSum, minLeftSubtreeElement, maxLeftSubtreeElement = traverse(node.left, float('-inf'), node.val)
            isRightSubtreeBST, rightSubTreeSum, minRightSubtreeElement, maxRightSubtreeElement = traverse(node.right, node.val, float('inf'))
            
            currSubtreeSum = leftSubTreeSum + rightSubTreeSum + node.val
            currIsValidBST = (
                isLeftSubtreeBST and \
                isRightSubtreeBST and \
                ((not node.left) or node.left.val < node.val) and \
                ((not node.right) or node.right.val > node.val) and \
                (maxLeftSubtreeElement < node.val < minRightSubtreeElement)
            )

            
            if currIsValidBST and currSubtreeSum > maxSum:
                maxSum = currSubtreeSum
                maxSumNode = node

                
            currMinVal = node.val
            currMaxVal = node.val
            
            if node.left:
                currMinVal = min(currMinVal, minLeftSubtreeElement)
                currMaxVal = max(currMaxVal, maxLeftSubtreeElement)
            
            if node.right:
                currMinVal = min(currMinVal, minRightSubtreeElement)
                currMaxVal = max(currMaxVal, maxRightSubtreeElement)

            return currIsValidBST, currSubtreeSum, currMinVal, currMaxVal

        traverse(root, float("-inf"), float("inf"))

        return maxSum