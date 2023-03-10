# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(-1, head)
        ptr1 = dummyNode
        ptr2 = dummyNode
        
        while ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            if not ptr2:
                break
            ptr2 = ptr2.next


        return ptr1
            
            