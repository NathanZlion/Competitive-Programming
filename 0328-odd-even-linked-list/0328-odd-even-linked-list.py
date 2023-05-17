# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next or not head.next.next:
            return head
        
        last_odd = head
        last_even = head.next
        first_even = last_even

        curr = last_even.next
        is_even = False
        
        while curr:
            if is_even:
                last_even.next = curr
                last_even = curr
            
            else:
                last_odd.next = curr
                last_odd = curr
            
            curr = curr.next
            is_even = not is_even

        last_odd.next = first_even
        last_even.next = None

        return head
            
        