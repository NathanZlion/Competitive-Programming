# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        currNode = head
        if not currNode: return None
        nextNode = currNode.next
        if not nextNode: return currNode
        currNode.next = nextNode.next
        nextNode .next = currNode
        currNode.next = self.swapPairs(currNode.next)
        return nextNode
