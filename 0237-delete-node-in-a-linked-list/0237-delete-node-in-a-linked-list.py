# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        curr = node
        nxt = curr.next
        while nxt.next:
            curr.val = nxt.val
            curr = nxt
            nxt = nxt.next
        curr.val = nxt.val
        curr.next = None
        
        
        
        
        