# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if left == right:
            return head

        dummyNode = ListNode(-1, head)
        curr = dummyNode

        for _ in range(left-1):
            curr = curr.next
        
        start = curr
        reverseStart = start.next

        for _ in range(right - left + 1):
            curr = curr.next
        
        reverseEnd = curr
        end = reverseEnd.next
        
        # reverse what's in between
        dummy = ListNode(-5, reverseStart)
        prev = dummy
        curr = reverseStart
        nxt = reverseStart.next
        reverseEnd.next = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        start.next = reverseEnd
        reverseStart.next = end
        
        return dummyNode.next
        
            
        
        
        