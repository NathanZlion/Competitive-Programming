# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # if either one is an empty linked list return the other one
        if not l1 or not l2:
            return l2 if not l1 else l1

        stack1 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        stack2= []
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        res = None
        carry = 0

        while stack1 or stack2 or carry:
            num = carry
            if stack1:
                num += stack1.pop()
            
            if stack2:
                num += stack2.pop()
            
            newNode = ListNode(val = num%10, next = res)
            newNode.next = res
            res = newNode
            carry = num//10

        return res
