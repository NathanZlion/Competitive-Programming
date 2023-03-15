# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        slowPointer, fastPointer = head, head.next
        
        stack = []
        
        while fastPointer:
            stack.append(slowPointer.val)
            
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next
            if fastPointer:
                fastPointer = fastPointer.next

        maxSum = 0
        while slowPointer:
            maxSum = max(maxSum, stack.pop() + slowPointer.val)
            slowPointer = slowPointer.next
        
        
        return maxSum
            
        