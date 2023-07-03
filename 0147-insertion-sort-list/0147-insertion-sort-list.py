# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(-1, head)
        prev, curr = head, head.next

        while curr != None:

            if curr.val>=prev.val:
                prev, curr= curr, curr.next
                continue

            # starting from head look for the right spot to insert curr node
            temp = dummy
            while curr.val > temp.next.val:
                temp=temp.next
                
            # inserting curr at the right spot
            prev.next = curr.next
            curr.next=temp.next
            temp.next=curr
            curr= prev.next

        return dummy.next