# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        counter = [0 for _ in range(201)]
        
        curr = head
        while curr:
            counter[curr.val + 100] += 1
            curr = curr.next
        
        dummyHead = ListNode(-101)
        curr = dummyHead
        
        for index, count in enumerate(counter):
            if count == 1:
                curr.next = ListNode(index - 100)
                curr = curr.next
        
        return dummyHead.next
                
                       
            
            
        
        