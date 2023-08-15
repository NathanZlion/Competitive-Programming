# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    @staticmethod
    def traverse(head: Optional[ListNode], x: int):
        before, after = [], []
        node = head
        while node:
            if node.val < x:
                before.append(node)
            else:
                after.append(node)
            node = node.next

        return before, after

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before, after = Solution.traverse(head, x)
        before.extend(after)
        dummyHead = ListNode()
        curr = dummyHead

        for node in before:
            curr.next = node
            curr = node

        curr.next = None
        return dummyHead.next
