# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummyHead = ListNode(-1, head)
        
        curr = dummyHead
        while curr:
            nxt = curr.next
            while nxt and nxt.val ==val:
                nxt = nxt.next
            curr.next = nxt
            curr = nxt
        
        return dummyHead.next