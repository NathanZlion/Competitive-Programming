# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(self, num1: int, num2: int) -> int:
        x, y = max(num1, num2), min(num1, num2)
        while(y):
            x, y = y, x % y

        return abs(x)

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        right = head.next
        left = head
        
        while right:
            _gcd = self.gcd(right.val, left.val)
            
            newNode = ListNode(_gcd, right)
            left.next = newNode
            left = right
            right = left.next

        return head