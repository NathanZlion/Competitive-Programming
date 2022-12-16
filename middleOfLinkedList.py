# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        flag = 0
        middleNode = currNode = head

        while not(currNode is None):
            flag += 1
            if flag == 2:
                middleNode = middleNode.next
                flag = 0
            currNode = currNode.next

        return middleNode
