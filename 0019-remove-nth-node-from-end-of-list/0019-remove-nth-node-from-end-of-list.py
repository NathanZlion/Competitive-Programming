# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummyNode = ListNode(-1, head)
        curr = dummyNode
        length = 0

        while curr.next:
            length += 1
            curr = curr.next
        
        curr = dummyNode
        for _ in range(length - n):
            curr = curr.next
        
        curr.next = curr.next.next

        return dummyNode.next
