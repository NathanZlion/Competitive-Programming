# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        curr = head
        if not curr: return curr

        while curr.next:
            nxt = curr.next
            if curr.val == nxt.val:
                curr.next = nxt.next

            else:
                curr = nxt
        
        
        return head
                
            
        