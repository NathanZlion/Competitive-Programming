# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = set()
        
        curr = head
        while curr and not curr in nodes:
            nodes.add(curr)
            curr = curr.next
        
        if curr:
            return curr
            