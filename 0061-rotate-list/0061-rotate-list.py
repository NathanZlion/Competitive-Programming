# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return head

        dummyHead = ListNode(-1, head)
        curr = dummyHead
        self.length = 0

        while curr.next:
            curr = curr.next
            self.length += 1

        # make it a circular linked list
        curr.next = head
        curr = dummyHead

        for _ in range(self.length-(k % self.length)):
            curr = curr.next

        res = curr.next
        curr.next = None

        return res

