# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
            
        currNode = head
        while currNode.next:
            nextNode = currNode.next
            currNode.next = nextNode.next
            nextNode.next= head
            head = nextNode

        return head
        
        
