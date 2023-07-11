# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()

        # traverse first linked list
        currNode = headA
        while currNode:
            visited.add(currNode)
            currNode = currNode.next

        # traverse second linked list and if visited before return the node
        currNode = headB
        while currNode:
            if currNode in visited:
                return currNode

            currNode = currNode.next
