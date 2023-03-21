# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverse(self, root: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = root

        if not root or not root.next: return root

        nxt = curr.next
        while curr:
            curr.next = prev
            prev = curr
            curr = nxt
            nxt = nxt.next if nxt else None

        return prev

    def merge(self, node1: Optional[ListNode], node2: Optional[ListNode]) -> None:
        while node1 and node2:
            next1 = node1.next
            next2 = node2.next

            node1.next = node2
            node2.next = next1
            node1 = next1
            node2 = next2

    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        - find the middle of the linked list
        - reverse the second half
        - merge the first half with the reversed second half
        '''
        # finding middle of linkedlist
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # by now slow points to the middle of the linked list
        secondHalfHead = self.reverse(slow.next)
        slow.next = None
        self.merge(head, secondHalfHead)
