# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def merge(self, list1, list2):
        
        if not list1:
            return list2

        if not list2:
            return list1

        if list1.val < list2.val:
            list1.next = self.merge(list1.next, list2)
            return list1

        list2.next = self.merge(list2.next, list1)
        return list2

        
    def middleNode(self, head):
        flag = 0
        middleNode = currNode = head

        while currNode:
            flag += 1
            if flag == 2:
                middleNode = middleNode.next
                flag = 0
            currNode = currNode.next

        return middleNode

    def sort(self, head):
        if not head:
            return None

        if not head.next:
            return head

        midPoint = self.middleNode(head)
        
        curr = head
        while not(curr.next is midPoint):
            curr = curr.next
        curr.next = None

        return self.merge(self.sort(head), self.sort(midPoint))

    def sortList(self, head):
        

        return self.sort(head)