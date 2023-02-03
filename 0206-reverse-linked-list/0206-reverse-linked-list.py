# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if not head or not head.next: return head
        
        prev = head
        curr = prev.next
        nxt = curr.next
        
        prev.next = None
        if not nxt:
            curr.next = prev
            return curr
        
        while nxt:
            curr.next = prev
            prev = curr
            curr = nxt
            nxt = nxt.next

        curr.next = prev
        return curr
        