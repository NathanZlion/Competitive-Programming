# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        valuesArr = []
        
        curr = head
        while curr:
            valuesArr.append(curr.val)
            curr = curr.next
        
        res = [0]*len(valuesArr)
        
        stack = []
        
        for index, value in enumerate(valuesArr):
            while stack and stack[-1][1] < value:
                prevIndex, _ = stack.pop()
                res[prevIndex] = value

            stack.append((index, value))
        
        return res