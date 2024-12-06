
class Node:
    
    def __init__(self, value: int, left: "Node" = None, right: "Node" = None):
        self.value = value
        self.left = left
        self.right = right

class SegmentTree:
    
    @staticmethod
    def construct(nums: List[int], left: int = 0, right: int = None) -> Node:
        right = right if right is not None else (len(nums) - 1)
        
        if left == right:
            return Node(nums[left])
        
        mid = (left + right) // 2
        # make a range
        leftChild = SegmentTree.construct(nums, left, mid)
        rightChild = SegmentTree.construct(nums, mid + 1, right)
        
        return Node(
            leftChild.value + rightChild.value,
            leftChild,
            rightChild
        )
    
    @staticmethod
    def update(segTreeNode: Node, index: int, value: int, left: int, right: int) -> int:
        if left == right == index:
            currVal = segTreeNode.value
            segTreeNode.value = value
            # return the change (delta)
            return (value - currVal)
        
        # decide to either go left or right
        mid = (left + right) // 2
        delta = None
        if index > mid:
            # go right
            delta = SegmentTree.update(segTreeNode.right, index, value, mid + 1, right)
        else:
            # go left
            delta = SegmentTree.update(segTreeNode.left, index, value, left, mid)
            
        segTreeNode.value += delta
        return delta
        
    @staticmethod
    def sumQuery(segTreeNode: Node, left: int, right: int, queryLeft : int, queryRight: int) -> int:
        if left == queryLeft and right == queryRight:
            return segTreeNode.value
        
        mid = (left + right) // 2
        res = 0
        
        # is left part queried
        if queryLeft <= mid:
            res += SegmentTree.sumQuery(segTreeNode.left, left, mid, queryLeft, min(queryRight, mid))

        # is right part queried
        if queryRight > mid:
            res += SegmentTree.sumQuery(segTreeNode.right, mid + 1, right, max(mid + 1, queryLeft), queryRight)

        return res

class NumArray:

    def __init__(self, nums: List[int]):
        self.segTree = SegmentTree.construct(nums)
        self.numElements = len(nums)

    def update(self, index: int, val: int) -> None:
        SegmentTree.update(self.segTree, index, val, 0, self.numElements - 1)

    def sumRange(self, left: int, right: int) -> int:
        return SegmentTree.sumQuery(self.segTree, 0, self.numElements - 1, left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)