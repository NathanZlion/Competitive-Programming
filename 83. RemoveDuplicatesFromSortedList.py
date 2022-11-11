# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        currNode = head
        if not currNode: return None
        while currNode and currNode.next:
            nextNode = currNode.next
            while nextNode and currNode.val == nextNode.val: nextNode=nextNode.next
            currNode.next = nextNode
            currNode = nextNode
        return head
