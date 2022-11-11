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
