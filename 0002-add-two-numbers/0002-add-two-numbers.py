# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        carry = 0
        
        ptr1 = l1
        ptr2 = l2
        
        dummyHead = ListNode()
        curr = dummyHead
        while ptr1 and ptr2:
            theSum = carry + ptr1.val + ptr2.val
            
            curr.next = ListNode(theSum%10)
            curr = curr.next
            carry = theSum//10
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        while ptr1:
            theSum = carry + ptr1.val
            
            curr.next = ListNode(theSum%10)
            curr = curr.next
            carry = theSum//10
            ptr1 = ptr1.next

            
        while ptr2:
            theSum = carry + ptr2.val
            
            curr.next = ListNode(theSum%10)
            curr = curr.next
            carry = theSum//10
            ptr2 = ptr2.next
        
        if carry > 0:
            curr.next = ListNode(carry)

        return dummyHead.next

            
            



