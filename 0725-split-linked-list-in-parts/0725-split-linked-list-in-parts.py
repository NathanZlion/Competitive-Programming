# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    @staticmethod
    def length(head: Optional[ListNode]) -> int:
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next

        return count

    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        res = [None]*k
        len_of_linkedlist = Solution.length(head)
        curr = head
        
        for index in range(k):
            # change the current at that point
            res[index] = curr
            
            # figure out the size of current partition
            curr_partition_size = (len_of_linkedlist//k)
            if (len_of_linkedlist%k) >= (index+1):
                curr_partition_size += 1

            i = 0
            while i < curr_partition_size-1 and curr:
                curr = curr.next
                i += 1
                
            if not curr:
                return res
            
            nxt = curr.next
            curr.next = None
            curr = nxt
        
        return res
        
        