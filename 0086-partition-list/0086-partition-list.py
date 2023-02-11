# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        
        curr = head
        before = []
        after = []
        while curr:
            if curr.val < x:
                before.append(curr.val)
            else:
                after.append(curr.val)
            
            curr = curr.next
        
        before.extend(after)
        
        curr = head
        for index in range(len(before)):
            curr.val = before[index]
            curr = curr.next
        
        return head
                