# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        curr = head
        nodeSet = set()
        while curr:
            if curr in nodeSet:
                return True
            nodeSet.add(curr)
            curr = curr.next
        
        return False
            
        