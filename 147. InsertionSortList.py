# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        prev, curr = head, head.next

        while curr:
            if curr.val>=prev.val:
                prev, curr= curr, curr.next
                continue
            # start at the head till you find the right spot, that is a node which is less than the curr
            temp = dummy
            while curr.val > temp.next.val:
                temp=temp.next
            # by now temp.next is greater than curr but not temp so insert curr in between temp and temp.next
            prev.next = curr.next
            curr.next=temp.next
            temp.next=curr
            curr= prev.next

        return dummy.next
