# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        length = 0
        curr = head
        
        while curr:
            curr = curr.next
            length += 1
        
        median = head
        mid = int(round(length/2))
        for _ in range(mid):
            median = median.next
        
        return median
        
        
