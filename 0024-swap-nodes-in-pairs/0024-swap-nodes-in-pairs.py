class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        if not head.next:
            return head
        
        
        curr = head.next
        head.next = self.swapPairs(curr.next)
        curr.next = head
                
        return curr
