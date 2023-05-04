# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def merge(self, node1: ListNode, node2: ListNode) -> ListNode:
        
        if not (node1 and node2):
            return node1 if node1 else node2

        if node1.val > node2.val:
            nextNode = node2.next
            node2.next = self.merge(node1, nextNode)
            return node2

        else:
            nextNode = node1.next
            node1.next = self.merge(node2, nextNode)
            return node1


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return 

        head = lists[0]
        for index in range(1, len(lists)):
            head = self.merge(head, lists[index])
        
        return head
            
            
        