# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        returnHead = front = back = ListNode(0, head)

        for _ in range(n):
            front = front.next
        
        while front.next != None:
            front = front.next
            back = back.next
        
        back.next = back.next.next        # Skip(remove) the intended node
        return returnHead.next
