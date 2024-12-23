# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def minSwapsToSortList(self, nums: List[int]) -> int:
        currIdx = { node: index for index, node in enumerate(nums)}
        numSwaps = 0
        
        sortedNum = sorted(nums)
        for index in range(len(nums)):
            if nums[index] != sortedNum[index]:
                indexToSwap = currIdx[sortedNum[index]]
                currIdx[nums[index]] = indexToSwap
                currIdx[nums[indexToSwap]] = index
                nums[index], nums[indexToSwap] = nums[indexToSwap], nums[index]
                
                numSwaps += 1
        
        return numSwaps

    
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        level = deque([root])
        totalSwaps = 0
        while level:
            arr = []
            for _ in range(len(level)):
                node : TreeNode = level.popleft()
                arr.append(node.val)
                
                if node.left:
                    level.append(node.left)
                
                if node.right:
                    level.append(node.right)
            
            totalSwaps += self.minSwapsToSortList(arr)
        
        return totalSwaps
