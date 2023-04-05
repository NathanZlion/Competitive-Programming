# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return
        slow = head
        fast = head
        
        while True:
            if not slow or not fast: return
            slow = slow.next
            fast = fast.next

            if not fast: return

            fast = fast.next

            if slow is fast:
                break

        curr = head

        while curr is not slow:
            curr = curr.next
            slow = slow.next


        return curr
