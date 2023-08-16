# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:    
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummyNode = ListNode(-1,head)
        end = dummyNode
        nodes_count = 0

        while end.next:
            end = end.next
            nodes_count += 1

        prev = dummyNode
        curr = dummyNode.next

        for _ in range(nodes_count):
            if curr.val >= x and curr.next:
                # remove it from that position
                prev.next = curr.next
                end.next = curr
                end = curr
                curr.next = None
                curr = prev.next
            else:
                prev = curr
                curr = curr.next

        return dummyNode.next
            