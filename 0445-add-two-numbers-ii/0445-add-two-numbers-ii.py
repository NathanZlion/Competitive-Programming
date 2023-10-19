# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        This shows that I have to put all nodes into a stack first then
        pop them to go from th stack
        """
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        place = 0  # 0th, 10th place ...
        carry = 0
        res = 0
        while stack1 or stack2 or carry > 0:
            curr_digit = 0
            if stack1:
                curr_digit += stack1.pop()

            if stack2:
                curr_digit += stack2.pop()

            curr_digit += carry
            carry = curr_digit // 10
            curr_digit %= 10
            res += curr_digit * (10**place)
            
            place += 1

        dummy_head = ListNode(-1)
        cur = dummy_head
        for c in str(res):
            cur.next = ListNode(int(c))
            cur = cur.next
        
        return dummy_head.next